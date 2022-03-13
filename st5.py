# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:25:51 2022

@author: vraj Thakar

video link:https://youtu.be/bsSBcByYaqQ

content
sidebar

"""
import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
import time 

plt.style.use("ggplot")

data = {
       "num":[x for x in range(1,11)],
       "twice":[x*2 for x in range(1,11)],
       "thrice":[x*3 for x in range(1,11)],
       "squre":[x**2 for x in range(1,11)] 
}

rad=st.sidebar.radio("Navigation",["home","about us"])
df = pd.DataFrame(data=data)
if rad == "home":
      st.sidebar.selectbox("select a number",[1,2,3,4,5])
      col=st.sidebar.selectbox("select a columns", df.columns) 
      plt.plot(df['num'],df[col])
      st.pyplot()

if rad=="about us": 
    progress= st.progress(0)
    for i in range (100):
        time.sleep(0.04)
        progress.progress(i+1)
    st.balloons()
        
    

    st.write("""
              contect:75749948940 \n
              wp:94884883993939 \n
              mail:vjkdkjhdfnj@gmail.com
               """)
    st.error("error")
    st.success("show success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("this is the warning")

    
 



