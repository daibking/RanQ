import requests
import time, random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    # 新增反爬请求头
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1"
}

# 在请求前添加随机延迟（防止高频访问）
time.sleep(random.uniform(0.5, 1.5))
# 发送请求
from urllib.parse import urlparse, urlunparse  # 新增URL解析模块

# url = str(input("请输入URL："))
url = "http://120.46.21.7:5000/" if input("使用默认网站（y/n）: ").lower() == 'y' else input("请输入URL：")

# 新增URL路径处理逻辑
parsed_url = urlparse(url)
if '/web/' in parsed_url.path:
    new_path = parsed_url.path.replace('/web/', '/proxies_status', 1)
else:
    new_path = parsed_url.path.rstrip('/') + '/proxies_status'

new_url = urlunparse(parsed_url._replace(path=new_path))
response = requests.get(new_url, headers=headers)  # 使用处理后的URL
response.encoding = response.apparent_encoding
json_data = response.json()    # 获取json数据

# 修复方案一：处理嵌套数据结构（假设代理信息在'proxies'字段中）
for proxy in json_data['proxies']:  # 修改遍历对象为嵌套字段
    # 添加协议类型判断
    if proxy['protocol'].lower() == 'socks5':  # 使用lower()兼容大小写
        print(f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}")

count = 0  # 初始化计数器
for proxy in json_data['proxies']:
    if proxy['protocol'].lower() == 'socks5':
        print(f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}")
        count += 1  # 每找到一个有效代理计数+1

print(f"\n=== 共找到 {count} 个SOCKS5代理 ===")  # 最终统计输出
