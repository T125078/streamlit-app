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
