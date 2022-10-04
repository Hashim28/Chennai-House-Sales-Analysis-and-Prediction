import streamlit as st
import numpy as np
import pickle
import xgboost
import pandas as pd
import datetime

def price_prediction(input_data):

  input_data_np_arr = np.asarray(input_data)
  input_data_reshaped = input_data_np_arr.reshape(1,-1)
  prediction = loaded_model.predict(input_data_reshaped)
  return prediction[0]


def main():
  st.title('Chennai House Price Prediction Web App')

  st.image("""https://miro.medium.com/max/720/0*YMZOAO8QE4bZ4_Rk.jpg""")

  st.header('Enter the house details:')

  Area = st.selectbox('Area',['Karapakkam','Adyar','Chrompet','Velachery','KK Nagar','Anna Nagar','T Nagar'])
  if(Area == 'Karapakkam'):
    area_no = 0
  elif(Area == 'Adyar'):
    area_no = 1
  elif(Area == 'Chrompet'):
    area_no = 2
  elif(Area == 'Velachery'):
    area_no = 3
  elif(Area == 'KK Nagar'):
    area_no = 4
  elif(Area == 'Anna Nagar'):
    area_no = 5
  elif(Area == 'T Nagar'):
    area_no = 6

  Sqft = st.text_input('Enter the Square Feet')

  n_bed = st.text_input('Enter the number of bedrooms')

  n_bath = st.text_input('Enter the number of bathrooms')

  n_room = st.text_input('Enter the number of rooms')

  park = st.selectbox('Is Parking facility available?',['Yes','No'])
  if park == 'Yes':
    park_no = 1
  else:
    park_no = 0
  
  utility = st.selectbox('Utility type',['ELO','No Sewer','All Public'])
  if utility == 'ELO':
    utility_no = 0
  elif utility == 'No Sewer':
    utility_no = 1
  else:
    utility_no = 2

  street = st.selectbox('Street Type',['No Access','Paved','Gravel'])
  if street == 'No Access':
    street_no = 0
  elif street == 'Paved':
    street_no = 1
  else:
    street_no = 2

  zone = st.selectbox('Zone Type',['A','C','I','RH','RL','RM'])
  if zone == 'A':
    zone_no = 0
  elif zone == 'C':
    zone_no = 1
  elif zone == 'I':
    zone_no = 2
  elif zone == 'RH':
    zone_no = 4
  elif zone == 'RL':
    zone_no = 5
  elif zone == 'RM':
    zone_no = 6

  build_date = st.date_input('Enter the house build date',min_value=datetime.date(year=1945, month=12, day=31))
  end_date = pd.to_datetime(datetime.date.today())
  age = end_date - pd.to_datetime(build_date)
  age = age / np.timedelta64(1,'D')

  buildtype = st.selectbox('Build type',['Commercial','House','Others'])  
  if(buildtype == 'Commercial'):
    commercial = 1
    house = 0
    other = 0
  elif(buildtype == 'House'):
    commercial = 0
    house = 1
    other = 0
  else:
    commercial = 0
    house = 0
    other = 1


  
  price = 0

  if st.button('Find the price'):
    price = price_prediction([area_no,Sqft,n_bed,n_bath,n_room,park_no,utility_no,street_no,zone_no,age,commercial,house,other])
    st.metric('Estmated Price, Rs',price)

if __name__ == '__main__':
  loaded_model = xgboost.XGBRegressor()
  loaded_model.load_model('price_prediction_model.pkl')

  main()
