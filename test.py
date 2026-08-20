import streamlit as st
import requests

st.title("我的即時匯率換算器 💱")

# 1. 準備兩張菜單和輸入金額的框框
from_currency = st.selectbox("我手上的幣種是：", ["TWD", "CNY", "JPY", "USD"])
to_currency = st.selectbox("我想換成：", ["CNY", "TWD", "JPY", "USD"])
amount = st.number_input("請輸入金額：", value=100)

# 2. 讓小信差帶著「我們手上的幣種」，去網路上查專屬的匯率表
# (注意網址最後面，我們把它換成了你在菜單上選的幣種！)
url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
data = requests.get(url).json()

# 3. 從小信差帶回來的匯率表裡面，找出我們「想換成」的那個幣種的匯率
target_rate = data["rates"][to_currency]

# 4. 算數學：金額 乘上 匯率，並用我們剛學過的 round 魔法把小數點變整齊（只留兩位）
result = round(amount * target_rate, 2)

# 5. 用廣播喇叭播報結果！
st.write("💵 換算結果是：", result, to_currency)