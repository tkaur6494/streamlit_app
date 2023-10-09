import streamlit
import pandas

streamlit.title("My Parents new Healthy Dinner")

streamlit.header("Breakfast Menu")
streamlit.text("Item 1")
streamlit.text("Item 2")
streamlit.text("Item 3")

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(fruit_list)

