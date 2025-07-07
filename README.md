\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{enumitem}

\title{\Huge{\textbf{🌍 趣旅星球 - 智能旅行规划助手}}}
\author{}
\date{}

\begin{document}

\maketitle

\section*{✨ 项目简介}
趣旅星球是一款使用Streamlit开发的智能旅行规划应用，它能根据你的出发地、目的地、旅行日期、预算和偏好，结合实时天气数据，生成详细的每日行程建议。无论是亲子游、美食探索还是户外冒险，都能为你量身打造最合适的旅行计划。

\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{screenshot.png} % 建议添加应用截图
    \caption{趣旅星球应用界面预览}
\end{figure}

\section*{🚀 核心功能}
\begin{itemize}[label=$\star$]
    \item 输入旅行基本信息（出发地、目的地、日期、预算）
    \item 选择旅行偏好（风景、文化、美食、购物等）
    \item 获取目的地未来天气预报
    \item 基于Gemini大模型生成个性化每日行程
    \item 包含景点推荐、活动安排、交通建议和住宿参考
    \item 响应式界面设计，操作简单直观
\end{itemize}

\section*{🛠️ 技术栈}
\begin{itemize}[label=$\circ$]
    \item \textbf{前端框架}：Streamlit
    \item \textbf{AI模型}：Google Gemini
    \item \textbf{天气数据}：OpenWeatherMap API
    \item \textbf{编程语言}：Python
\end{itemize}

\section*{🔧 安装与使用}

\subsection*{前提条件}
\begin{itemize}
    \item Python 3.8+
    \item Gemini API密钥（可从\href{https://aistudio.google.com/}{Google AI Studio}获取）
    \item OpenWeatherMap API密钥（可从\href{https://openweathermap.org/}{OpenWeatherMap官网}获取）
\end{itemize}

\subsection*{安装步骤}
\begin{verbatim}
# 克隆仓库
git clone https://github.com/你的用户名/qulvxingqiu.git
cd qulvxingqiu

# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run app.py
\end{verbatim}

\subsection*{使用流程}
1. 在浏览器中访问显示的本地地址（通常是http://localhost:8501）  
2. 在侧边栏输入你的Gemini API密钥和OpenWeatherMap API密钥  
3. 填写旅行信息并点击"生成旅行计划"按钮

\section*{📝 使用示例}
\begin{enumerate}
    \item 出发地：杭州
    \item 目的地：三亚
    \item 旅行日期：选择2023-10-01至2023-10-05（共5天）
    \item 预算：5000元
    \item 偏好：美食、休闲、风景
    \item 点击生成按钮，获取包含每日行程和天气建议的旅行计划
\end{enumerate}

\section*{📌 注意事项}
\begin{itemize}
    \item API密钥请妥善保管，不要泄露给他人
    \item 免费的OpenWeatherMap API有调用频率限制
    \item Gemini API可能会产生使用费用，请参考官方定价
    \item 行程建议仅供参考，实际出行前请确认景点开放情况和交通信息
\end{itemize}

\section*{🤝 贡献指南}
欢迎提交Issues和Pull Requests来帮助改进这个项目！
\begin{enumerate}
    \item Fork本仓库
    \item 创建你的特性分支（\texttt{git checkout -b feature/amazing-feature}）
    \item 提交你的修改（\texttt{git commit -m 'Add some amazing feature'}）
    \item 推送到分支（\texttt{git push origin feature/amazing-feature}）
    \item 打开一个Pull Request
\end{enumerate}

\section*{📄 许可证}
本项目采用MIT许可证 - 详见LICENSE文件

\section*{🌟 致谢}
\begin{itemize}
    \item \href{https://streamlit.io/}{Streamlit} - 简单易用的Python web框架
    \item \href{https://ai.google.dev/}{Google Gemini} - 强大的大语言模型
    \item \href{https://openweathermap.org/}{OpenWeatherMap} - 提供天气数据支持
\end{itemize}

\vspace{2cm}
如有任何问题或建议，欢迎提交Issue或联系我！

\end{document}
