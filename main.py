import streamlit as st
import plotly_express as px
import pandas as pd


header = st.beta_container()
dtataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()

st.sidebar.subheader("settings")

UploadedFile = st.sidebar.file_uploader(
    label="upload a csv or excel file!. (200mb max)",
type=['csv', 'xlsx'])

global df
if UploadedFile is not None:
    print(UploadedFile)
    print("hello")
    try:
         df = pd.read_csv(UploadedFile)
    except Exception as e:
        print("e")
        df = pd.read_excel(UploadedFile)
    
try:
     st.write(df)
except Exception as e:
 print(e)
 st.write("plese upload file")



with dtataset:
    st.header("data file")


