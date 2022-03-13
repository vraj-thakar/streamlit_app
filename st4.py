# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:35:44 2022

@author: vraj Thakar
videolink:https://youtu.be/r50Dr0APzAI
file uploded, number input, date, time, text_input, slider, radio, selct, checkbox, multiselect

following code about the widgets (streamlit app is intetractive using widgets
"""

import streamlit as st

st.title("widgets")
if st.button("subscribe"):
    st.write("thank you")

name=st.text_input("Name")
if name:st.write("ensure that, Is your name {} ?".format(name))

adrees= st.text_input("enter your adrees here.")

#date 
st.date_input("enter your date bourth.")
#time
st.time_input("enter current time.")

t_c=st.checkbox("you accept the t&c.")
if t_c:st.write("you accepted and turst on our policy",'"THANK YOU!"')

#radio button (mcq)
rd=st.radio("collours",["b","g","y"],index=1) #index is ddefault selected
if rd=="b": st.write("you have selecte blue")
if rd=="g": st.write("you have selecte green")
if rd=="y": st.write("you have selecte yellow")

#select box 

sel=st.selectbox("collours",["b","g","y"],index=2)

#multiselect

m_s=st.multiselect("collours",["b","g","y"])
if m_s: st.write(m_s) #it return dictonary

#rm_s=st.radio_multisel#muli select question
st.write('Select three known variables:')
option_s = st.checkbox('displacement (s)')
option_u = st.checkbox('initial velocity (u)')
option_v = st.checkbox('final velocity (v)')
option_a = st.checkbox('acceleration (a)')
option_t = st.checkbox('time (t)')
known_variables = option_s + option_u + option_v + option_a + option_t

if known_variables <3:
    st.write('You have to select minimum 3 variables.')
elif known_variables == 3:
   st.write('Now put the values of your selected variables in SI units.')
elif known_variables >3:
    st.write('You can select maximum 3 variables.')
    
#slider 

age= st.slider("age",min_value=1, max_value=150,value=30) #default value
if age<=12:st.write("you are Child")
if age>=13 and age<=18:st.write("you are Teanager")
if age>=19 and age<=59:st.write("you are Adult")
if age>=60:st.write("you are senior Adult")

#number input 
st.number_input("numbers",min_value=18.0, max_value=60.0,step=0.5)

#file uploded
img=st.file_uploader("uplod your file")
st.image(img)
