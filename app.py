import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
import requests
from datetime import date

# --------------- Streamlit 设置 ---------------
st.set_page_config(page_title="趣旅星球", page_icon="🌍", layout="wide")

st.title("✈️ 趣旅星球——智能旅行规划助手")
st.markdown("使用 Gemini 和 OpenWeatherMap，为你生成个性化旅行行程建议")

# --------------- API 密钥设置 ---------------
with st.sidebar:
    st.header("🔑 API 密钥配置")
    gemini_key = st.text_input("Gemini API Key", type="password")
    weather_key = st.text_input("OpenWeatherMap API Key", type="password")

    ready = gemini_key and weather_key
    if ready:
        st.success("✅ 密钥配置完成")
    else:
        st.warning("⚠️ 请填写完整 API 密钥")

# --------------- 用户输入区域 ---------------
col1, col2 = st.columns(2)
with col1:
    source = st.text_input("出发地", placeholder="如 杭州")
    destination = st.text_input("目的地", placeholder="如 三亚")
    dates = st.date_input("旅行日期", [date.today(), date.today()])
with col2:
    budget = st.number_input("预算（元）", min_value=0, max_value=20000, step=100)
    preferences = st.multiselect("旅行偏好", ["风景", "文化", "美食", "购物", "亲子", "自然", "冒险", "休闲"])

days = (dates[1] - dates[0]).days + 1 if len(dates) == 2 else 1

# --------------- 天气数据获取函数（OpenWeatherMap） ---------------
def get_weather(city, days, key):
    try:
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": city,
            "appid": key,
            "units": "metric",
            "lang": "zh_cn"
        }
        r = requests.get(url, params=params)
        if r.status_code != 200:
            return f"❌ 请求失败：{r.status_code} - {r.text}"
        
        data = r.json()

        if "list" not in data:
            return f"❌ 数据格式异常：{data}"

        forecast_text = f"📍 {city} 未来天气预报：\n"
        shown_dates = set()

        for item in data["list"]:
            date_str = item["dt_txt"].split()[0]
            if date_str not in shown_dates:
                desc = item["weather"][0]["description"]
                temp = item["main"]["temp"]
                rain = item.get("pop", 0) * 100
                forecast_text += f"📅 {date_str}：{desc}，{temp:.1f}°C，降雨概率 {rain:.0f}% 🌧️\n"
                shown_dates.add(date_str)
                if len(shown_dates) >= min(days, 3):
                    break

        return forecast_text

    except requests.exceptions.RequestException as e:
        return f"❌ 网络请求异常：{e}"
    except Exception as e:
        return f"⚠️ 天气获取失败：{e}"

# --------------- Gemini 旅行助手 Agent ---------------
def run_travel_agent(gemini_key, weather_info, user_info):
    model = Gemini(id="gemini-2.5-flash-preview-05-20", api_key=gemini_key)
    agent = Agent(
        name="旅行规划助手",
        role="根据用户信息与天气预报，生成个性化的旅行计划",
        model=model,
        instructions=[
            "你是一名专业旅行规划师。",
            "根据用户信息、偏好、预算和天气预报，为其制定每日详细行程建议。",
            "输出需包含景点、活动、交通、住宿建议，中文回答，多加点emoji表情，适合普通人阅读。",
            "结合天气情况提出建议或提醒。"
        ]
    )
    return agent.run(f"{user_info}\n\n天气预报：\n{weather_info}")

# --------------- 提交按钮与处理 ---------------
if st.button("🎯 生成旅行计划", disabled=not ready):
    if not source or not destination:
        st.error("❌ 请填写出发地和目的地")
    else:
        with st.spinner("✈️ 正在为您生成旅行计划..."):
            try:
                weather = get_weather(destination, days, weather_key)
                user_info = f"""
出发地：{source}
目的地：{destination}
出发日期：{dates[0]}
返回日期：{dates[1]}
预算：{budget} 元
偏好：{', '.join(preferences) or '无'}
                """
                response = run_travel_agent(gemini_key, weather, user_info)
                st.success("✅ 旅行计划已生成")
                st.markdown(response.content if hasattr(response, "content") else response)
            except Exception as e:
                st.error(f"生成失败：{e}")

