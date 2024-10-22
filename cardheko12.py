# import datetime
# import joblib
import streamlit as st
import pickle
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
# from scipy.linalg import _fblas


    
st.title("🚗Cardheko Price Prediction 🚗")

st.markdown("##### Are you planning to sell your car🚗 !?\n##### So let's try evaluating the price.. 🤖 ")

st.write('')

st.write('')


filename ='C:/Users/SG_LENOVO/Downloads/random_model.pkl'
load_model=pickle.load(open(filename, 'rb'))

# with open(r"random_model.pkl", 'rb') as s:
#     trained_model = pickle.load(s)

Car_Age = st.number_input('Car Age ?',1, 20, step=1, key ='age')
Age_old = 20-Car_Age

modelYear=st.number_input('Model Year  ?',2010, 2024, step=1, key ='modelYear')
Model_y = 2024-modelYear

model_encoded =st.selectbox('Car Model name?',('Maruti', 'Ford','Hyundai','BMW', 'Renault', 'Audi'),key='car')
if(model_encoded=='Maruti'):
    model_encoded=1
    car_model_Ford=0
elif(model_encoded=='Ford'):
    model_encoded=0
    car_model_Ford=1
else:
    model_encoded=0
    car_model_Ford=0


centralVariantId_t= st.slider(' Central Variant Id of Car?', 0.00, 10000.00, step=1000.00, key ='centralVariantId_t')
# if(centralVariantId_t=='Third Party insurance'):
#     centralVariantId_t=1
#     Insurance_c=0
# elif(centralVariantId_t=='Comprehensive'):
#     centralVariantId_t=0
#     Insurance_c=1
# else:
#     centralVariantId_t=0
#     Insurance_c=0


Kms_Driven = st.number_input('Distance completed by the car in Kilometers ?', 0.00, 50000.00, step=100.00, key ='drived')

No_of_owners = st.radio("The number of owners the car had previously ?", (1, 2,3,4,5), key='owner')

# seats = st.radio("The number of seats the car had ?", (3,4,5,6), key='seats')

mileage_kmpl = st.slider('What is mileage  by the car ?', 0.00, 100.00, step=10.00, key ='mileage')

Engine_cc = st.slider('What is Engine CC  by the car ?', 0.00, 10000.00, step=1000.00, key ='Engine')


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
        #st.write(model_encoded)
        prediction = tr_Model.predict([[No_of_owners,modelYear,Kms_Driven,centralVariantId_t, Car_Age,mileage_kmpl, model_encoded, Transmission_Manual,Body_Type_h, Fuel_Type_Petrol,City_chennai ]])
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





