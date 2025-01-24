# Import libraries
import streamlit as st

# Add a title
st.title("Air BnB : A Data-Driven Analysis")
st.write("A Streamlit project by MM, EB & MS.")
st.sidebar.title("Table of contents")
# Create three pages
pages=["Exploration", "DataVizualization", "Modelling"]
page=st.sidebar.radio("Go to", pages)

# Write "Presentation of data" at the top of the first page
if page == pages[0] : 
  st.write("### Presentation of data")
  
  
# Write "DataVizualization" at the top of the second page
if page == pages[1] : 
  st.write("### DataVizualization")

  
# Write "Modelling" at the top of the third page
if page == pages[2] : 
  st.write("### Modelling")
