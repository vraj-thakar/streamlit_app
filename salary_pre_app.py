import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt # use for Non Interactive graph
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False) #You can disable this warning by disabling the config option:
st.title("salary predictor")
data=pd.read_csv("./salary_data.csv")
x= np.array(data["YearsExperience"]).reshape(-1,1)

lr = LinearRegression()
lr.fit(x, np.array(data["Salary"]))
nav=st.sidebar.radio("Navigation",["Home","prediction","contribute"],index=0)
if nav=="Home":
    st.image("salary.jpg",width=800)
    if st.checkbox("Show Our Source Data"):
        st.table(data)
    graph = st.selectbox("what kind of Graph",["Non-interactive","Interactive"])
    val = st.slider("filter data using years",1.0,16.0)
    data = data.loc[data["YearsExperience"]>=val]
    if graph == "Non-interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"], data["Salary"])
        plt.ylim(0)
        plt.xlabel("YearsExperience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
        
    if graph == "Interactive":
        layout = go.Layout(
            xaxis =dict(range=[0,16]), #year of experiance
            yaxis =dict(range=[0,210000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode="markers"),layout=layout)
        st.plotly_chart(fig)

if nav=="prediction":
    st.header("know your Salary")
    st.image("your_salary.jpg")
    val = st.number_input("Enter youe Year of Experiance",0.0,20.0,step=0.25)
    val = np.array(val).reshape(-1,1)
    pred= lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your salary is :{round(pred)}")



if nav=="contribute":
    st.header("contribute to our dataset")
    st.image("con_salary.jpg")
    ex= st.number_input("Enter your Experiance ",0.0,20.0,step=0.25)
    sal = st.number_input("Enter your Salary",0.0,1000000.0,step=1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode='a',header = False,index= False)
        st.success("Submitted")        

