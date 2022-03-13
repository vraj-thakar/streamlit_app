# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:56:06 2022

@author: vraj Thakar
"""

import streamlit as st
import numpy as np
import pandas as pd
import time
a=[1,2,3,4,3,3]
n=np.array(a)
nd=n.reshape(3,2)
dic={ "name":["ngv","khgh","mhvbh"],
     "age":[78,78,9],
     "city":["jhjkhg","gfjghhj","mncjg"]
     
     }
data = pd.read_csv("E:/vraj pr/data science/data sets/Toyota.csv")
st.dataframe(data,height=600,width=600)
st.dataframe(nd)
st.dataframe(dic)
#if data ius small
st.table(dic)

st.json(dic)

st.write(data)

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()
if st.checkbox("1"):
    st.write(ret_time(1))
if st.checkbox("2"):
    st.write(ret_time(2))
