# Hello World Flask 应用

这是一个简单的 Flask Hello World 应用程序，展示了基本的 Web 开发功能。

## 功能特性

- 🎯 现代化的响应式设计
- 📱 移动端友好界面
- 🔄 实时时间显示
- 📊 JSON API 接口
- 👤 个性化问候功能
- 🎨 渐变色彩设计

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
python app.py
```

应用将在 http://localhost:5000 启动

## 页面路由

- `/` - 主页，显示 Hello World 和学生信息
- `/api/hello` - API 接口，返回 JSON 数据
- `/hello/<name>` - 个性化问候页面

## 项目结构

```
├── app.py              # Flask 应用主文件
├── requirements.txt    # Python 依赖包
├── templates/          # HTML 模板目录
│   └── index.html     # 主页模板
└── README.md           # 项目说明文档
```

## 学生信息

- **学号**: 20231201020
- **姓名**: 彭方冠

## 技术栈

- **后端**: Flask 2.3.3
- **前端**: HTML5, CSS3, JavaScript
- **样式**: 现代化渐变设计
- **响应式**: 移动端适配

## 开发说明

这个应用展示了：
1. Flask 路由配置
2. 模板渲染
3. API 接口开发
4. 响应式网页设计
5. 学生信息展示

## 许可证

MIT License