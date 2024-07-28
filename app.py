import numpy as np
import pandas as pd
import streamlit as st

# Load data
data = pd.read_csv("C:\\Users\\DELL\\Desktop\\My Notebooks\\Projects\\data.csv")

# Streamlit sidebar title
st.sidebar.title("Companies Review")

# List of unique states from the data
list_of_state = list(data['state'].unique())

# Streamlit selectbox for state selection
selected_state = st.sidebar.selectbox("Select a State Where You Want to Start a Business", list_of_state)

# Filter data for the selected state
state = data[data['state'] == selected_state]

# Get the top 3 industries in the selected state
top_3_industry = state['industry'].value_counts().head(3)
top_3_industry_df = pd.DataFrame(top_3_industry).reset_index()
top_3_industry_df.columns = ['Industry', 'Count']

# Get the top 3 cities in the selected state
top_3_cities = state['city'].value_counts().head(3)
top_3_cities_df = pd.DataFrame(top_3_cities).reset_index()
top_3_cities_df.columns = ['City', 'Count']

# Display the title and top 3 industries
st.title("The top 3 Industries in the State are")
st.write(top_3_industry_df)

# Best Cities inside that State
st.title("The top 3 cities in the State are")
st.write(top_3_cities_df)
