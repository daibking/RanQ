from flask import Flask, render_template

app = Flask(__name__)

# 网络安全蓝队常用系统命令数据
commands = [
    {
        "name": "ping",
        "description": "用于测试网络连接，向目标主机发送 ICMP 回显请求并等待响应。",
        "example": "ping 8.8.8.8"
    },
    {
        "name": "traceroute",
        "description": "用于跟踪数据包从源主机到目标主机所经过的路由。",
        "example": "traceroute 8.8.8.8"
    },
    {
        "name": "nmap",
        "description": "强大的网络扫描工具，可用于发现主机、端口扫描等。",
        "example": "nmap -sV 192.168.1.0/24"
    },
    {
        "name": "netstat",
        "description": "显示网络连接、路由表、网络接口等信息。",
        "example": "netstat -an"
    },
    {
        "name": "whois",
        "description": "查询域名或 IP 地址的注册信息。",
        "example": "whois example.com"
    },
    {
        "name": "dig",
        "description": "用于 DNS 解析，查询 DNS 记录。",
        "example": "dig example.com"
    },
    {
        "name": "whois",
        "description": "查询域名或 IP 地址的注册信息。",
        "example": "whois example.com"
    }
]


@app.route('/')
def index():
    return render_template('index.html', commands=commands)


if __name__ == '__main__':
    app.run(debug=True)
    