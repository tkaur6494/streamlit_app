import streamlit
import pandas

streamlit.title("My Parents new Healthy Dinner")

streamlit.header("Breakfast Menu")
streamlit.text("Item 1")
streamlit.text("Item 2")
streamlit.text("Item 3")

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

strea,lit.dataframe(fruit_list)

