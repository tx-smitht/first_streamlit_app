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



# new section
st.header("Code for Joel")

code = '''{
  "2\\" GPM": {
    "N": "4.38801615"
  },
  "2\\" Minutes of Flow": {
    "N": "12.333333333333334"
  },
  "3/4\\" GPM": {
    "N": "0"
  },
  "3/4\\" Minutes of Flow": {
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
} '''

st.code(code, language='json')


snowpark_code = ''' 
# Load the data from the NEPTUNE_DATA_RAW table
df_table = session.table('NEPTUNE_DATA_RAW')

# Print off 1 record
df_table.select(col('raw_data')['Item']).show(1)

# Say which elements we want as columns. Put in list to be iterated through
col_list = ['2\" GPM','timestamp', '2\" Minutes of Flow', '3/4\" Minutes of Flow', '3/4\" GPM', 'Inlet Pressure', 'Outlet Pressure',
            'Current State 1', 'Current State 2', 'baseline_prediction','multivariate_v2_prediction','retraining_model_prediction']

# List that will hold the column selection statements
column_selection_statements = []

# Build column selection statements
for column in col_list:
    if column == 'timestamp':
        column_selection_statements.append(col("raw_data")['Item'][column]['N'].cast(IntegerType()).alias(column[0:5]))
    else:
        column_selection_statements.append(col("raw_data")['Item'][column]['N'].cast(FloatType()).alias(column[0:5]))


# Query using the column selection statements
df_clean_table = df_table.select(column_selection_statements).order_by('TIMES',ascending=False)
df_clean_table.show(10)'''

st.code(snowpark_code, language='python')
