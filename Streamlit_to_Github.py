# Import libraries
import streamlit as st

# Add a title
st.title("Air BnB : A Data-Driven Analysis")

### SIDEBAR CONFIGURATION ###

st.sidebar.image("AirBnB/airbnb.jpg", width=300)

st.sidebar.title("Table of contents")
# Create six pages
pages=["Introduction", "Data Exploration and Preprocessing", "Data Visualization", "Data Modelling", "Prediction", "Conclusion"]
page=st.sidebar.radio("Go to", pages)

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

#Path to logo file
logo_url = 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/notebooks/looker_studio/logo_datascientest.png'

st.sidebar.markdown(
  f"""
  <style>
    .sidebar-content {{
        text-align: center;}}

    .sidebar-content img {{
        width: 50px; 
        margin: 10px 0;}}

    </style>
    <div class="sidebar-content">
      <p><i><b>A Datascientest project carried out by </br> Ecem BOZKAYA </br> Marta MURAWSKA </br> Matthew SELWYN </br> </i></p>
      <p><i><b>Project mentor: Tarik Anouar</b></i></p>
      <img src="{logo_url}" alt="Logo">
      <p>Data Analyst Training </br> December 2024 Cohort</p>
    </div>
    """,
    unsafe_allow_html=True)









# Write "Presentation of data" at the top of the first page
if page == pages[0] : 
  st.write("### INTRODUCTION")  
  st.write("Airbnb is a global online marketplace that connects travellers with hosts offering short-term stays in unique accommodations, including spare rooms, shared rooms, and even entire homes and apartments. Since its creation in 2008, it has revolutionised the travel industry by enabling peer-to-peer rentals, but the platform has also faced criticism for its impact on housing markets and local communities, prompting regulatory responses in many cities.")
  st.write("The short-term rental market is highly competitive, with hosts constantly adjusting prices to attract guests while maximising revenue. This project looks at the many factors which influence the price of a listing on AirBnb. Understanding the relationship between these factors and price is valuable for travellers looking for certain features within a certain budget. But it is also essential knowledge for a host looking to maximise their rental property, and has implications on the wider travel industry, influencing  pricing trends and market fluctuations.")
  st.write("To execute this project, we chose to analyse datasets from Inside Airbnb, a platform that provides detailed information and insights about Airbnb listings in cities around the world. Our analysis focuses on datasets for Paris, France that were compiled in September 2024.") 
  st.write("### OBJECTIVE")
  st.write("The overall objective of this project is to build a predictive Machine Learning model capable of forecasting price for a given set of variables, such as property type, location and number of beds, and then evaluate our findings.")
  st.write("In order to achieve this, we need to start by conducting exploratory data analysis (EDA) on our datasets to identify which are the key influencing variables on price. Here we can visualise the data to identify trends and relationships between price and the numerous property variables.")
  st.write("To ensure data quality, the data will then need to be processed and cleaned, before we can use it to train and build our Machine Learning models.")

  
  
# Write "Data Exploration" at the top of the second page
if page == pages[1] : 
  st.write("### Data Exploration")

  
# Write "Data Visualisation" at the top of the third page
if page == pages[2] : 
  st.write("### Data Visualisation")


# Write "Data Modelling" at the top of the fourth page
if page == pages[3] : 
  st.write("### Data Modelling")
  st.write('Hello Marta & Elyssa')


# Write "Prediction" at the top of the fifth page
if page == pages[4] : 
  st.write("### Prediction")


# Write "Conclusion" at the top of the sixth page
if page == pages[5] : 
  st.write("### Conclusion")
  st.write("This project aimed to analyze the key factors influencing Airbnb pricing in Paris and develop predictive models to optimize pricing strategies. Through extensive data analysis, we identified that factors such as property type, number of reviews, review scores, and proximity to landmarks are crucial determinants of accommodation prices. Additionally, attributes like the number of bathrooms, bedrooms, and available beds played a notable role, emphasizing the importance of space and comfort for guests.")
  st.write("The best-performing model was the <b>Random Forest Regression</b>, with R² values of 0.242 for the test set, and the lowest MAE (29.177) and RMSE (36.320). This model provided the most accurate pricing predictions, balancing accuracy and error minimization. While regression models like Random Forest provided the best results for predicting continuous price values, the Random Forest Classifier showed 88.2% accuracy for classification tasks and solid performance across all categories.")
  st.write("For Airbnb hosts, our analysis offers valuable insights to optimize pricing strategies. Offering 'Entire Unit' accommodations, maintaining high review scores, optimizing space (through bathrooms, bedrooms, and beds), and positioning properties near key landmarks like the Eiffel Tower are strategies that can enhance occupancy and revenue.")
  st.write("While our analysis provided robust insights, future work can delve deeper by exploring seasonal pricing trends, the impact of specific amenities on guest satisfaction, or expanding the analysis to other cities. Incorporating more advanced machine learning techniques could further refine predictive accuracy and provide deeper insights into the dynamic short-term rental market.")
