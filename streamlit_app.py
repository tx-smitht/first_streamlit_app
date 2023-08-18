import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title('My Parents\' Healthy Diner')

st.header('Breakfast Menu')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
st.dataframe(fruits_to_show)

# new section
st.header("Fruityvice Fruit Advice!")

fruit_choice = st.text_input('What fruit would you like info about?', 'Kiwi')
st.write(f'the User entered {fruit_choice}')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalize the json using pandas
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Show the normalized json
st.dataframe(fruityvice_normalized)

st.code('{
  "2\" GPM": {
    "N": "4.38801615"
  },
  "2\" Minutes of Flow": {
    "N": "12.333333333333334"
  },
  "3/4\" GPM": {
    "N": "0"
  },
  "3/4\" Minutes of Flow": {
    "N": "0"
  },
  "Current State 1": {
    "N": "0"
  },
  "Current State 2": {
    "N": "1"
  },
  "Inlet Pressure": {
    "N": "68.450148"
  },
  "Outlet Pressure": {
    "N": "65.227448"
  },
  "multivariate_v2_prediction": {
    "N": "5.4966981451"
  },
  "retraining_model_prediction": {
    "N": "2.1368063366"
  },
  "timestamp": {
    "N": "1692191353"
  }
}, language='json')
