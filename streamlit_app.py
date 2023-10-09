import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title("My Parents new Healthy Dinner")

streamlit.header("Breakfast Menu")
streamlit.text("Item 1")
streamlit.text("Item 2")
streamlit.text("Item 3")

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruit_list.index), ["Avocado", "Strawberries"])

fruits_to_show = fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")



fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
