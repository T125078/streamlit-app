import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
st.dataframe(df,width=800,height=220)

#データ抽出
with st.sidebar:
  year = st.multiselect("年",
                          df["year"].unique())
  month = st.multiselect("月",
                          df["month"].unique())
