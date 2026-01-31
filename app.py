import streamlit as st
import pandas as pd
import plotly.express as px
import time
import streamlit.components.v1 as components

#1秒間待機
with st.spinner("Wait for it..."):
  time.sleep(1)

components.html("<script>alert('ようこそ')</script>")

st.title("Webアプリを作ってみた!")

#使い方
st.subheader("使い方")
how_to_use = st.selectbox("使い方を知りたい項目を選んでください",["AAA","BBB"])
if st.button("使い方確認"):
  components.html(f"<script>alert('{how_to_use}の使い方を確認します。')</script>")


#データフレーム作成
df = pd.read_csv("Data.csv")

#データ抽出
with st.sidebar:
  st.write("表に使うデータ抽出")
  year = st.multiselect("年",
                          df["year"].unique())
  month = st.multiselect("月",
                          df["month"].unique())

df = df[df["year"].isin(year)]
df = df[df["month"].isin(month)]
st.dataframe(df,width=800,height=220)
st.divider()

#グラフ用データ抽出
dfg_o = pd.read_csv("Data.csv")
with st.sidebar:
  st.write("グラフに使うデータ抽出")
  select_1 = st.selectbox("x軸",
                          ["国内総生産(支出側)","民間最終消費支出","家計最終消費支出","民間住宅","民間企業設備","民間在庫変動","政府最終消費支出"])
  select_2 = st.selectbox("y軸(1)",
                          ["国内総生産(支出側)","民間最終消費支出","家計最終消費支出","民間住宅","民間企業設備","民間在庫変動","政府最終消費支出"])
  select_3 = st.selectbox("y軸(2)",
                          ["国内総生産(支出側)","民間最終消費支出","家計最終消費支出","民間住宅","民間企業設備","民間在庫変動","政府最終消費支出"])
  
fig = px.scatter(dfg_o,
                 x=select_1,
                 y=select_2,
                 title=f"{select_1} vs {select_2}")
st.plotly_chart(fig)
st.divider()

fig = px.scatter(dfg_o,
                 x=select_1,
                 y=[select_2,select_3],
                 title=f"{select_1} vs {select_2} vs {select_3}")
st.plotly_chart(fig)