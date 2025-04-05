
# 网络安全常用命令展示网站

这是一个基于 Flask 和 Vue 3 的网络安全命令展示网站，提供了常用的蓝队命令，命令分类、搜索功能，并可点击查看命令详情。

## 项目结构

```
project/
├── backend/               # Flask 后端
│   ├── app.py             # Flask 应用代码
│   ├── commands.json      # 存储网络安全命令数据
│   ├── templates/         # 存放 Flask 渲染的 HTML 文件
│   │   └── index.html     # Vue 挂载点
│   └── static/            # 存放前端构建的静态文件
│
├── frontend/              # Vue + Vite 前端项目
│   ├── index.html         # 前端入口 HTML 文件
│   ├── vite.config.js     # Vite 配置文件
│   ├── package.json       # Node.js 项目依赖
│   └── src/               # 前端源代码
│       ├── main.js        # Vue 入口文件
│       ├── App.vue        # Vue 组件文件
│       └── components/    # 子组件目录
│           ├── CommandCard.vue  # 命令卡片组件
│           └── CommandModal.vue # 命令弹窗组件
```

## 环境要求

- Python 3.6+ (用于运行 Flask 后端)
- Node.js 16+ (用于运行 Vue 前端)
- `pip` (Python 包管理工具)
- `npm` (Node.js 包管理工具)

## 安装和运行

### 1. 安装 Flask 后端依赖

进入 `backend/` 文件夹，安装 Python 依赖：

```bash
cd backend
pip install -r requirements.txt
```

### 2. 安装前端依赖

进入 `frontend/` 文件夹，安装 Node.js 依赖：

```bash
cd frontend
npm install
```

### 3. 启动 Flask 后端

在 `backend/` 文件夹内运行 Flask：

```bash
cd backend
python app.py
```

Flask 后端将会在 `http://127.0.0.1:5000/` 启动。

### 4. 启动前端开发服务器

在 `frontend/` 文件夹内运行 Vite：

```bash
cd frontend
npm run dev
```

前端将会在 `http://127.0.0.1:5173/` 启动。

### 5. 构建前端静态文件

如果你想将前端文件构建到 Flask 后端的静态文件夹中，可以运行以下命令：

```bash
cd frontend
npm run build
```

这将会把构建后的静态文件放置在 `frontend/dist/` 目录下。然后，你可以将这些文件移到 Flask 后端的 `static/` 目录中。

### 6. 部署

你可以将该项目部署到任意支持 Flask 的服务器上，如：

- Heroku
- DigitalOcean
- AWS EC2
- Nginx + Gunicorn

## 命令数据格式

`commands.json` 文件存储了命令的详细信息，包括命令名称、分类、描述和执行命令。格式如下：

```json
{
  "name": "netstat",
  "category": "网络监控",
  "description": "显示网络连接、路由表、接口统计等信息。",
  "command": "netstat -tuln"
}
```

你可以在 `commands.json` 中添加更多的命令，根据自己的需求更新数据。

## 功能

- **命令分类**：所有命令按类别分组显示。
- **搜索功能**：可以通过输入命令名称或描述进行搜索。
- **弹窗展示**：点击命令卡片后，会弹出模态框显示命令详情。

## 扩展

你可以根据项目需求扩展以下功能：

1. **命令复制功能**：为每个命令添加复制按钮，方便用户复制命令。
2. **命令标签**：为每个命令添加标签（如 Linux/Windows），方便用户筛选。
3. **分页显示**：对于命令数量较多的情况，可以加入分页功能。

## 贡献

欢迎提交 PR 或报告问题！如果你有更好的想法或功能，欢迎提出。

## 许可证

MIT 许可证，详见 LICENSE 文件。
