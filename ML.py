import warnings
warnings.filterwarnings('ignore')
import streamlit as sl
import pickle
import numpy  as np
import pandas as pd
with open("model.pkl","rb") as file:
    model=pickle.load(file)
X=pd.read_csv("x.csv")
sl.html(f"""<div style="background-color:#bde0fe;">
        <h1 style="color:#007ea7;text-align:center;">BANGLORE HOUSE PREDICTIONS<h1>
        </div>""")
with sl.form("form1"):
    size=sl.number_input("enter bhk",placeholder=2.0,step=1.0)
    sqft=np.log1p(sl.number_input("enter your total square feet",placeholder=1056.0,step=1.0))
    bath=sl.number_input("enter number of bathrooms",placeholder=2.0,step=1.0)
    balcony=sl.number_input("enter number of balconies",placeholder=1.0,step=1.0)
    loc=sl.selectbox("enter location",options=X.columns[4:222])
    area=sl.radio("select area type",options=X.columns[222:])
    def analyze(size,sqft,bath,balcony,loc,area,model):
        X=pd.read_csv("x.csv")
        lis=[]
        lis.append(size)
        lis.append(sqft)
        lis.append(bath)
        lis.append(balcony)
        for i in X.columns[4:]:
            if i==loc or i==area:
                lis.append(1)
            else:
                lis.append(0)
        pred=model.predict([lis])
        sl.write(f"price is aprox {np.expm1(pred)[0]}")
    sl.form_submit_button("get price",on_click=analyze(size,sqft,bath,balcony,loc,area,model))
sl.markdown("""<style>
            .stNumberInput{
            background-color:#bde0fe;
            }
            .st-emotion-cache-ysk9xe.e1nzilvr5{
            color:#274c77;
            }
            .st-emotion-cache-76z9jo.e116k4er2{
            color:green;
            }
            .stTextInput{
            background-color:#bde0fe;
            }
            .stForm{
            background-color:#bde0fe;
            }
            .st-emotion-cache-1y5f4eg.e1nzilvr5{
            color:green;
            text-align:center;
            background-color:#efebce;
            }
            .st-emotion-cache-3lmqu2.e1nzilvr5{
            color:#f9844a;
            }
            </style>""",unsafe_allow_html=True)
sl.html("""<h5 style="color:red;">Note:THE PREDICTIONS WERE BASED ON MY MODEL ITS ACCURACY IS 73% SO THERE MIGHT BE DIFFERENCES IN PRICES</H5>""")
