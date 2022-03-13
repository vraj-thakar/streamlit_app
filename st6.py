# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:10:35 2022

@author: vraj Thakar
"""
import streamlit as st

st.title("Registration form")

first,last = st.columns(2)

f_n=first.text_input("First Name")
l_n=last.text_input("Last Name")
email,mob = st.columns([3,1])
E=email.text_input("Enter email")
M=mob.text_input("Mobile Number")

user,pw,pw2 = st.columns(3)
U= user.text_input("User Name")
Pw=pw.text_input("password",type="password")
Pw2=pw2.text_input("Retype your password",type="password")

if Pw!=Pw2:st.write("try again(passwordd missmatched)")

ch,b1,sub=st.columns(3)

ch.checkbox("I agree all t&c")
sub.button("Submit")

