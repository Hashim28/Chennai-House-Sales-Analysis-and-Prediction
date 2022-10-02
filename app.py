import streamlit as st
import numpy as np
import pickle
import xgboost
from xgboost import XGBRegressor


def price_prediction(input_data):

  loaded_model = pickle.load(open('price_prediction_model.pkl','rb'))

  input_data_np_arr = np.asarray(input_data)
  input_data_reshaped = input_data_np_arr.reshape(1,-1)
  prediction = loaded_model.predict(input_data_reshaped)
  return prediction[0]


def main():
  st.title('Chennai House Price Prediction Web App')

  st.markdown('**Area:**')
  st.text('0 - Karapakkam, 1 - Adyar, 2 - Chrompet, 3 - Velachery,4 - KK Nagar,5 - Anna Nagar,6 - T Nagar')
  Area = st.text_input('Enter the Area in number')

  st.markdown('**Squae Feet:**')
  Sqft = st.text_input('Enter the Square Feet')

  st.markdown('**Bedroom:**')
  n_bed = st.text_input('Enter the number of bedrooms')

  st.markdown('**Bathroom:**')
  n_bath = st.text_input('Enter the number of bathrooms')

  st.markdown('**Room:**')
  n_room = st.text_input('Enter the number of rooms')

  st.markdown('**Parking Facility:**')
  st.text('1 - Parking facility available, 0 - Parking facility not available')
  park = st.text_input('Enter availability of Parking facility in number')
  
  st.markdown('**Utility type:**')
  st.text('0 - ELO, 1 - No Sewer, 2 - All Public')
  utility = st.text_input('Enter the type of Utility available in number')
  
  st.markdown('**Street Type**:')
  st.text('0 - No Access, 1 - Paved, 2 - Gravel')
  street = st.text_input('Enter the type of street in number')

  st.markdown('**Zone Type:**')
  st.text('0 - A, 1 - C, 2 - I, 4 - RH, 5 - RL, 6 - RM')
  zone = st.text_input('Enter the type of Zone in number')

  st.markdown('**House age:**')
  age = st.text_input('Enter the house age in days')

  st.markdown('**Build Type:**')
  st.text('1 - Commercial, 2 - House, 3 - Others')
  buildtype = st.text_input('Enter the Build type in number')  
  if(buildtype == '1'):
    commercial = 1
    house = 0
    other = 0
  elif(buildtype == '2'):
    commercial = 0
    house = 1
    other = 0
  else:
    commercial = 0
    house = 0
    other = 1


  
  price = 0

  if st.button('Find the price'):
    price = price_prediction([Area,Sqft,n_bed,n_bath,n_room,park,utility,street,zone,age,commercial,house,other])
    st.metric('Estmated Price, Rs',price)

if __name__ == '__main__':
  main()
