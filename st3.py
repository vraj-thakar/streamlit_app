# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:44:00 2022

@author: vraj Thakar

video link:https://youtu.be/jq0lKFb-P8k
folling code is about charts, graph, map, audio, video, image etc.
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

data=pd.DataFrame(np.random.randn(100,3),columns=["a","b","c"])

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
plt.scatter(data["a"], data["b"])
plt.title("dlkfe")
st.pyplot(plt.show())


chart= alt.Chart(data).mark_circle().encode(
    x="a", y="b", tooltip=["a","b"]
    )
st.altair_chart(chart)

st.graphviz_chart("""
                  digraph{
                      watch->like
                      like->share
                      share->subscribe
                      subscribe->watch
                      
                      
                      
                      }
                  
                  
                  
                  
                  """)
            
#world map
st.map()       

st.image("")

st.audio("")
st.video("")