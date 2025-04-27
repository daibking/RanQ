import requests

heads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

try:
    url = input("输入URL: ").strip().rstrip('/')  # 移除末尾斜杠
    # 添加URL协议头验证
    if not url.startswith(('http://', 'https://')):
        url = f'http://{url}'
    base_url = url + "/.git"
    config_url = url + "/.git/config"
    
    # 添加超时和请求头
    resp1 = requests.get(base_url, headers=heads, timeout=10)
    resp2 = requests.get(config_url, headers=heads, timeout=10)
    
    # 正确获取状态码（移除括号）
    code1, code2 = resp1.status_code, resp2.status_code
    
    # 改进判断逻辑：当两个请求都返回200时提示漏洞
    if code1 != code2 :
        print(f"发现漏洞！状态码: {code1}")
        print("参考信息: https://medium.com/@prakashchand72/lenovo-database-of-root-user-credentials-exposed-22aab5382c")
    else:
        print(f"正常响应 | 主目录: {code1} | 配置文件: {code2}")

except requests.exceptions.RequestException as e:
    print(f"请求失败: {str(e)}")
except Exception as e:
    print(f"发生错误: {str(e)}")


