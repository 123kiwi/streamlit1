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
  st.write("INTRODUCTION")
  st.write("Airbnb is a global online marketplace that connects travellers with hosts offering short-term stays in unique accommodations, including spare rooms, shared rooms, and even entire homes and apartments. Since its creation in 2008, it has revolutionised the travel industry by enabling peer-to-peer rentals, but the platform has also faced criticism for its impact on housing markets and local communities, prompting regulatory responses in many cities.")
  st.write("The short-term rental market is highly competitive, with hosts constantly adjusting prices to attract guests while maximising revenue. This project looks at the many factors which influence the price of a listing on AirBnb. Understanding the relationship between these factors and price is valuable for travellers looking for certain features within a certain budget. But it is also essential knowledge for a host looking to maximise their rental property, and has implications on the wider travel industry, influencing  pricing trends and market fluctuations.")
  st.write("To execute this project, we chose to analyse datasets from Inside Airbnb, a platform that provides detailed information and insights about Airbnb listings in cities around the world. Our analysis focuses on datasets for Paris, France that were compiled in September 2024.") 
  st.write("OBJECTIVE")
  st.write("The overall objective of this project is to build a predictive Machine Learning model capable of forecasting price for a given set of variables, such as property type, location and number of beds, and then evaluate our findings. 
In order to achieve this, we need to start by conducting exploratory data analysis (EDA) on our datasets to identify which are the key influencing variables on price. Here we can visualise the data to identify trends and relationships between price and the numerous property variables. 
To ensure data quality, the data will then need to be processed and cleaned, before we can use it to train and build our Machine Learning models.
")

  
  
# Write "DataVizualization" at the top of the second page
if page == pages[1] : 
  st.write("### DataVizualization")

  
# Write "Modelling" at the top of the third page
if page == pages[2] : 
  st.write("### Modelling")
