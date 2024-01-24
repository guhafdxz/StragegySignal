import streamlit as st
import pandas as pd
import numpy as np



st.markdown("水晶球🔮")
st.sidebar.markdown("水晶球🔮")

st.header('加密市场看板')

col1, col2, col3,col4 = st.columns(4)

with col1:
   st.caption("BTC市值和统治力")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.caption("ETH市值和汇率")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col3:
   st.caption("BTC和股指")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col4:
   st.caption("BTC和黄金")
   st.image("https://static.streamlit.io/examples/cat.jpg")

col5, col6, col7,col8 =  st.columns(4)

with col5:
    st.caption("美元利率和M2")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col6:
    st.caption("USDT流动性")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col7:
    st.caption("非农就业和核心CPI")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col8:
    st.caption("ETF流入和流出")
    st.image("https://static.streamlit.io/examples/cat.jpg")

col9, col10, col11,col12 =  st.columns(4)

with col9:
    st.caption("DeFi链上TVL")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col10:
    st.caption("NFT成交量")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col11:
    st.caption("跨链桥Bridge")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col12:
    st.caption("Ordinal铭文")
    st.image("https://static.streamlit.io/examples/cat.jpg")


col13, col14, col15,col16 =  st.columns(4)

with col13:
    st.caption("期货未平仓")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col14:
    st.caption("期货多空比")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col15:
    st.caption("期权波动率")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col16:
    st.caption("期权费率")
    st.image("https://static.streamlit.io/examples/cat.jpg")
