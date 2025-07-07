🌍 趣旅星球 - 智能旅行规划助手
基于 Gemini 大模型和 OpenWeatherMap 的个性化旅行计划生成工具，帮你轻松搞定旅行中的行程安排！
✨ 项目简介
趣旅星球是一款使用 Streamlit 开发的智能旅行规划应用，它能根据你的出发地、目的地、旅行日期、预算和偏好，结合实时天气数据，生成详细的每日行程建议。无论是亲子游、美食探索还是户外冒险，都能为你量身打造最合适的旅行计划。


界面预览
image
（建议添加一张应用截图）
🚀 核心功能
输入旅行基本信息（出发地、目的地、日期、预算）
选择旅行偏好（风景、文化、美食、购物等）
获取目的地未来天气预报
基于 Gemini 大模型生成个性化每日行程
包含景点推荐、活动安排、交通建议和住宿参考
响应式界面设计，操作简单直观
🛠️ 技术栈
前端框架：Streamlit
AI 模型：Google Gemini
天气数据：OpenWeatherMap API
编程语言：Python
🔧 安装与使用
前提条件
Python 3.8+
Gemini API 密钥（可从 Google AI Studio 获取）
OpenWeatherMap API 密钥（可从 OpenWeatherMap 官网 获取）
安装步骤
克隆仓库
bash
git clone https://github.com/你的用户名/qulvxingqiu.git
cd qulvxingqiu

安装依赖
bash
pip install -r requirements.txt

（requirements.txt 应包含：streamlit、agno、requests 等）
运行应用
bash
streamlit run app.py

在浏览器中访问显示的本地地址（通常是 http://localhost:8501）
在侧边栏输入你的 Gemini API 密钥和 OpenWeatherMap API 密钥
填写旅行信息并点击 "生成旅行计划" 按钮
📝 使用示例
出发地：杭州
目的地：三亚
旅行日期：选择 2023-10-01 至 2023-10-05（共 5 天）
预算：5000 元
偏好：美食、休闲、风景
点击生成按钮，获取包含每日行程和天气建议的旅行计划
📌 注意事项
API 密钥请妥善保管，不要泄露给他人
免费的 OpenWeatherMap API 有调用频率限制
Gemini API 可能会产生使用费用，请参考官方定价
行程建议仅供参考，实际出行前请确认景点开放情况和交通信息
🤝 贡献指南
欢迎提交 Issues 和 Pull Requests 来帮助改进这个项目！

Fork 本仓库
创建你的特性分支 (git checkout -b feature/amazing-feature)
提交你的修改 (git commit -m 'Add some amazing feature')
推送到分支 (git push origin feature/amazing-feature)
打开一个 Pull Request
📄 许可证
本项目采用 MIT 许可证 - 详见 LICENSE 文件
🌟 致谢
Streamlit - 简单易用的 Python web 框架
Google Gemini - 强大的大语言模型
OpenWeatherMap - 提供天气数据支持
