import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import time

#3秒間待機
with st.spinner("Wait for it..."):
  time.sleep(3)

st.title("Webアプリを作ってみた!")
