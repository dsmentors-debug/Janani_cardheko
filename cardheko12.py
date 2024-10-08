import datetime
import joblib
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score,make_scorer


    
st.title("🚗Cardheko Price Prediction 🚗")

st.markdown("##### Are you planning to sell your car🚗 !?\n##### So let's try evaluating the price.. 🤖 ")

st.write('')

st.write('')


filename =r'C:\Users\SG_LENOVO\Downloads\random_forest.pkl'
load_model=pickle.load(open(filename, 'rb'))



Car_Age = st.number_input('How much car age ?',1, 20, step=1, key ='age')
Age_old = 20-Car_Age


car_model_Maruti =st.selectbox('which model you want?',('Maruti', 'Ford','Hyundai','BMW', 'Renault', 'Audi'),key='car')
if(car_model_Maruti=='Maruti'):
    car_model_Maruti=1
    car_model_Ford=0
elif(car_model_Maruti=='Ford'):
    car_model_Maruti=0
    car_model_Ford=1
else:
    car_model_Maruti=0
    car_model_Ford=0


Insurance_t=st.selectbox('What is the body type of the car ?',('Third Party insurance','Comprehensive', ), key='Insurance')
if(Insurance_t=='Third Party insurance'):
    Insurance_t=1
    Insurance_c=0
elif(Insurance_t=='Comprehensive'):
    Insurance_t=0
    Insurance_c=1
else:
    Insurance_t=0
    Insurance_c=0


Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=1000.00, key ='drived')

Owner = st.radio("The number of owners the car had previously ?", (1, 2,3,4,5), key='owner')

seats = st.radio("The number of seats the car had ?", (3,4,5,6), key='seats')

mileage_kmpl = st.slider('What is mileage  by the car ?', 0.00, 100.00, step=10.00, key ='mileage')


Body_Type_h=st.selectbox('What is the body type of the car ?',('Hatchback','SUV', 'Sedan'), key='Body_Type')
if(Body_Type_h=='Hatchback'):
    Body_Type_h=1
    Body_Type_SUV=0
elif(Body_Type_h=='SUV'):
    Body_Type_h=0
    Body_Type_SUV=1
else:
    Body_Type_h=0
    Body_Type_SUV=0


Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
if(Fuel_Type_Petrol=='Petrol'):
    Fuel_Type_Petrol=1
    Fuel_Type_Diesel=0
elif(Fuel_Type_Petrol=='Diesel'):
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=1
else:
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=0

 
Transmission_Manual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
if(Transmission_Manual=='Manual'):
     Transmission_Manual=1
else:
    Transmission_Manual=0


City_chennai =st.selectbox('which city ?',('chennai', 'kolkata','delhi','jaipur', 'bangalore', ),key='city')
if(City_chennai=='chennai'):
    City_chennai=1
    city_chennai=0
elif(City_chennai=='kolkata'):
    City_chennai=0
    City_Kolkata=1
else:
    City_chennai=0
    City_Kolkata=0


if st.button("Estimate Price", key='predict'):
        tr_Model = load_model  #get_model()
        prediction = tr_Model.predict([[Insurance_t,Kms_Driven, Owner, Car_Age,mileage_kmpl,seats, car_model_Maruti, Transmission_Manual,Body_Type_h, Fuel_Type_Petrol,City_chennai ]])
        output = round(prediction[0],2)
        if output<0:
            st.warning("You will be not able to sell this car !!")
        else:
            st.success("You can sell the car for {} lakhs 🙌".format(output))
            st.balloons()


# some information about the project

st.header( 'Little information about the project')
prj_info = """
            Here you can predict used car 🚗" price by giving some information like model fo the car, fuel type, kilometer, 
            mileage, transmission, and then click on estimate price ,
            I recommend here to use 'Random forest Regressor' for 
            predicting the car price.

"""

st.write(prj_info)





