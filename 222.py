import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from datetime import datetime, timedelta

# 設定頁面
st.set_page_config(page_title="🌍 能源未來模擬器", layout="wide", page_icon="🌞")

# 標題與導航
st.title("🌍 能源未來模擬器")
st.markdown("""
探索可再生能源、碳足跡與氣候變遷的互動模擬平台
""")

# 創建導航選項卡
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 首頁", "⚡ 發電模擬", "👣 碳足跡計算", 
    "💰 碳交易市場", "❓ 能源問答", "📊 未來預測"
])

# 首頁 - 宣傳動畫
with tab1:
    st.header("歡迎來到能源未來模擬器！")
    
    # 簡單的動畫效果
    with st.expander("🎬 觀看能源轉型動畫", expanded=True):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            if i < 25:
                status_text.text("🌱 正在模擬植樹造林...")
            elif i < 50:
                status_text.text("☀️ 正在安裝太陽能板...")
            elif i < 75:
                status_text.text("💨 正在建設風力發電...")
            else:
                status_text.text("⚡ 電網綠色化進行中...")
            time.sleep(0.02)
        
        progress_bar.empty()
        status_text.success("✅ 能源轉型完成！碳排放減少60%！")
    
    # 統計數據卡片
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("全球升溫", "1.2°C", "-0.3°C")
    with col2:
        st.metric("再生能源占比", "35%", "12%")
    with col3:
        st.metric("碳價格", "$45/吨", "$15")
    
    st.markdown("---")
    st.subheader("開始探索：")
    st.info("使用上方選項卡來探索不同的能源主題！")

# 發電模擬
with tab2:
    st.header("⚡ 發電組合模擬器")
    
    # 發電比例調整滑桿
    col1, col2, col3 = st.columns(3)
    with col1:
        coal = st.slider("燃煤發電 (%)", 0, 100, 40)
        gas = st.slider("燃氣發電 (%)", 0, 100, 20)
    with col2:
        nuclear = st.slider("核能發電 (%)", 0, 100, 10)
        hydro = st.slider("水力發電 (%)", 0, 100, 8)
    with col3:
        solar = st.slider("太陽能發電 (%)", 0, 100, 12)
        wind = st.slider("風力發電 (%)", 0, 100, 10)
    
    total = coal + gas + nuclear + hydro + solar + wind
    if total != 100:
        st.warning(f"發電比例總和為 {total}%，請調整至100%")
    else:
        # 計算碳排放
        emissions = (coal * 0.95 + gas * 0.45 + nuclear * 0.05 + 
                    hydro * 0.01 + solar * 0.02 + wind * 0.01)
        
        # 顯示結果
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("發電結構")
            fig, ax = plt.subplots()
            sources = ['燃煤', '燃氣', '核能', '水力', '太陽能', '風力']
            sizes = [coal, gas, nuclear, hydro, solar, wind]
            colors = ['#666666', '#FF9999', '#66B2FF', '#0066CC', '#FFCC00', '#99CCFF']
            ax.pie(sizes, labels=sources, colors=colors, autopct='%1.1f%%')
            st.pyplot(fig)
        
        with col2:
            st.subheader("環境影響")
            st.metric("碳排放強度", f"{emissions:.2f} kgCO₂/kWh")
            st.metric("預計年碳排放", f"{emissions * 8760:.0f} 吨")
            st.metric("相當於植樹", f"{(emissions * 8760 / 0.022):.0f} 棵")

# 碳足跡計算
with tab3:
    st.header("👣 個人碳足跡計算器")
    
    st.subheader("交通方式")
    car_km = st.slider("每週開車里程 (公里)", 0, 500, 100)
    bus_km = st.slider("每週公車里程 (公里)", 0, 300, 50)
    train_km = st.slider("每週火車里程 (公里)", 0, 200, 30)
    
    st.subheader("能源使用")
    electricity = st.slider("每月用電量 (度)", 0, 1000, 300)
    gas_usage = st.slider("每月瓦斯使用 (m³)", 0, 100, 20)
    
    st.subheader("飲食習慣")
    meat_meals = st.slider("每週肉食餐數", 0, 21, 7)
    local_food = st.select_slider("本地食物比例", options=["很少", "一些", "一半", "大部分", "全部"])
    
    # 計算碳足跡
    transport_co2 = (car_km * 0.2 + bus_km * 0.08 + train_km * 0.05) * 52
    energy_co2 = electricity * 0.5 + gas_usage * 2.0
    food_co2 = meat_meals * 5.0 * 52
    
    total_co2 = transport_co2 + energy_co2 + food_co2
    
    st.success(f"您的年碳足跡估計為: {total_co2:.0f} kgCO₂")
    st.info("""
    **對比數據**:
    - 台灣人均年碳足跡: ~10,000 kgCO₂
    - 全球目標年碳足跡: ~2,000 kgCO₂
    """)

# 碳交易市場模擬
with tab4:
    st.header("💰 碳權交易模擬市場")
    
    st.subheader("當前市場狀況")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("碳權價格", "$45.60", "+$2.30")
    with col2:
        st.metric("交易量", "1.2M", "+150K")
    with col3:
        st.metric("市場情緒", "看漲", "")
    
    st.subheader("你的投資組合")
    initial_cash = 10000
    carbon_credits = st.slider("購買碳權數量", 0, 100, 20)
    cash_remaining = initial_cash - carbon_credits * 45.60
    
    st.write(f"現金餘額: ${cash_remaining:.2f}")
    st.write(f"碳權持有: {carbon_credits} 單位")
    
    # 模擬市場波動
    if st.button("模擬一年市場變化"):
        price_change = random.uniform(-10, 20)
        new_price = 45.60 + price_change
        portfolio_value = cash_remaining + carbon_credits * new_price
        
        st.metric("新的碳權價格", f"${new_price:.2f}", f"{price_change:+.2f}")
        st.metric("投資組合價值", f"${portfolio_value:.2f}", 
                 f"{(portfolio_value - 10000):+.2f}")

# 能源問答遊戲
with tab5:
    st.header("❓ 能源知識挑戰")
    
    questions = [
        {
            "question": "太陽能板在陰天能發電嗎？",
            "options": ["完全不能", "效率降低但仍可發電", "比晴天更有效率"],
            "answer": 1
        },
        {
            "question": "以下哪種能源的碳排放最高？",
            "options": ["風力發電", "燃煤發電", "核能發電"],
            "answer": 1
        },
        {
            "question": "碳交易的主要目的是什麼？",
            "options": ["賺取利潤", "減少溫室氣體排放", "促進國際貿易"],
            "answer": 1
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"問題 {i+1}")
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        if st.button(f"檢查答案 {i+1}", key=f"btn{i}"):
            if q["options"].index(answer) == q["answer"]:
                st.success("✅ 正確！")
                score += 1
            else:
                st.error("❌ 錯誤！")
            st.write(f"正確答案: {q['options'][q['answer']]}")
    
    if score > 0:
        st.success(f"你的得分: {score}/{len(questions)}")

# 未來預測
with tab6:
    st.header("📊 能源未來預測")
    
    year = st.slider("選擇預測年份", 2025, 2050, 2035)
    
    # 簡單的預測模型
    renewable_growth = (year - 2025) * 1.5
    coal_decline = (year - 2025) * 0.8
    emissions_reduction = (year - 2025) * 2.0
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{year}年預測")
        st.metric("再生能源占比", f"{20 + renewable_growth:.1f}%")
        st.metric("燃煤發電占比", f"{40 - coal_decline:.1f}%")
        st.metric("碳排放減少", f"{emissions_reduction:.1f}%")
    
    with col2:
        st.subheader("情境比較")
        scenario = st.selectbox("選擇情境", 
                              ["現行政策", "積極轉型", "技術突破"])
        
        if scenario == "積極轉型":
            bonus = 15
        elif scenario == "技術突破":
            bonus = 25
        else:
            bonus = 0
            
        st.info(f"在{scenario}情境下，再生能源可額外增加{bonus}%")

# 頁腳
st.markdown("---")
st.caption("🌱 本模擬器僅用於教育目的，數據為簡化估算 | 打造永續未來需要每個人的參與")