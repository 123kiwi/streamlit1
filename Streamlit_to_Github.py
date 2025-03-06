# Import required libraries
import streamlit as st
from PIL import Image


# Custom CSS for text justification
st.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a title
st.title("Air BnB : A Data-Driven Analysis")

### SIDEBAR CONFIGURATION ###

st.sidebar.image("AirBnB/airbnb.jpg", width=300)

st.sidebar.title("Table of contents")
# Create six pages
pages = ["Introduction & Objective", "Data Audit & Exploration", "Data Cleaning & Preparation", 
         "Exploratory Data Visualization", "Data Optimization & Feature Engineering", 
         "Machine Learning Models", "Prediction", "Conclusion"]
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


# Page Content
if page == pages[0]:
    st.header("Welcome to our project!")
    st.markdown(
        """
        <div class="justified-text">
        Airbnb is a global online marketplace that connects travellers with hosts offering short-term stays in unique accommodations, including spare rooms, shared rooms, and even entire homes and apartments. Since its creation in 2008, it has revolutionised the travel industry by enabling peer-to-peer rentals, but the platform has also faced criticism for its impact on housing markets and local communities, prompting regulatory responses in many cities.🌍✈️<br><br>

        The short-term rental market is highly competitive, with hosts constantly adjusting prices to attract guests while maximising revenue. 📅📈💰 
        This project looks at the many factors which influence the price of a listing on Airbnb. 
        Understanding the relationship between these factors and price is valuable for travellers looking for certain features within a certain budget.<br>

        It is also essential knowledge for a host looking to maximise their rental property, and has implications on the wider travel industry, influencing pricing trends and market fluctuations.<br><br>
        <p style='font-size:19px; font-weight:bold'>
        Ready to find out what turns an Airbnb listing into the hottest spot in town? 🔥 🚀
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display an image with the correct parameter
    st.image("AirBnB/Airbnb_real.jpg", use_container_width=True)

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[1]:
    st.header("Data Audit & Exploration")
    st.markdown(
        """
        <div class="justified-text">
        To execute this project, we chose to analyse datasets from <a href="https://insideairbnb.com/" target="_blank">Inside Airbnb</a>, a platform that provides detailed information and insights about Airbnb listings in cities around the world. Our analysis focuses on datasets for Paris, France that were compiled on 6 September 2024. 🌍📊<br><br>

        The data utilizes public information compiled from the Airbnb website including price, availability, and reviews for each listing. No private information is being used, as all names, listings, and review details are publicly displayed on the Airbnb site. 🔍💼<br>

        The platform has datasets from 117 cities from around the world, and for this project we chose to focus on Paris. 🗼<br><br>
        More details can be found at: <a href="https://insideairbnb.com/get-the-data/" target="_blank">Inside Airbnb Paris</a>.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="justified-text">
        <h3>📂Dataset: Airbnb Listings Data (<i>listings.csv.gz</i>)</h3>
        
        <b> → Volume:</b> 75 columns / 95,461 rows. The data types are a mixture of <i>object</i>, <i>int64</i>, and <i>float64</i> values, with 35 of the columns containing categorical data.<br>
        
        <b> → Missing Values:</b> 29 of the columns had some amount of data missing.<br>
        
        From our initial inspection of the data, it became clear very quickly that <b>'price'</b> would make a very interesting target variable to model for.<br>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="justified-text">
        It was also immediately apparent that we would not need to keep all of the columns for our analysis. 
        Instead, we focused on the most potent ones, which we determined could influence the price, including:<br><br>
        
        • <i>property_type</i><br>
        • <i>latitude</i><br>
        • <i>longitude</i><br>
        • <i>bathrooms_text</i><br>
        • <i>bedrooms</i><br>
        • <i>beds</i><br>
        • <i>price</i><br>
        • <i>number_of_reviews</i><br>
        • <i>review_scores_rating</i><br>
        </div>
        """,
        unsafe_allow_html=True
    )
    import streamlit as st
    import pandas as pd

    

    st.markdown(
        """
        <div class="justified-text">
        <h3> 📂Property Type🏠🏙️ </h3>
        
        <div class="justified-text">
        Our dataset has 70 different property types. Many are standard types such as <i>'Entire home'</i> and <i>'Private room in townhouse'</i>, but there are also some unusual categories listed, such as <i>'Boat'</i>, <i>'Castle'</i>, and even <i>'Cave'</i>! 🛶🏰🕳️<br><br>


        Of the 70 different property types, only 13 featured in more than 100 listings. These 13 property types represent more than 99% of the dataset. We filtered out all those that featured less than 100 times.<br>

        Curious to see if these 13 property types could be filtered further into categories, we created 3 subcategories and tested them for price correlation:<br>
        
        • <i>'Entire Unit'</i><br>
        • <i>'Private Room'</i><br>
        • <i>'Shared Room'</i><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display the property type table
    st.markdown(
        """
        <div class="justified-text">

        <table>
            <tr><th>Property Type</th><th>Frequency</th><th>Category</th></tr>
            <tr><td>Entire rental unit</td><td>80,176</td><td>Entire Unit</td></tr>
            <tr><td>Private room in rental unit</td><td>5,997</td><td>Private Room</td></tr>
            <tr><td>Entire condo</td><td>2,621</td><td>Entire Unit</td></tr>
            <tr><td>Room in boutique hotel</td><td>1,225</td><td>Private Room</td></tr>
            <tr><td>Room in hotel</td><td>1,084</td><td>Private Room</td></tr>
            <tr><td>Entire loft</td><td>975</td><td>Entire Unit</td></tr>
            <tr><td>Entire home</td><td>659</td><td>Entire Unit</td></tr>
            <tr><td>Private room in bed and breakfast</td><td>594</td><td>Private Room</td></tr>
            <tr><td>Private room in condo</td><td>341</td><td>Private Room</td></tr>
            <tr><td>Entire serviced apartment</td><td>291</td><td>Entire Unit</td></tr>
            <tr><td>Entire townhouse</td><td>272</td><td>Entire Unit</td></tr>
            <tr><td>Shared room in rental unit</td><td>263</td><td>Shared Room</td></tr>
            <tr><td>Private room in home</td><td>123</td><td>Private Room</td></tr>
        </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section 5.2: Number of Bedrooms & Bathrooms
    st.subheader("📂Number of Bedrooms & Bathrooms🛏️🛀")
    st.markdown(
        """
        <div class="justified-text">
        The dataset has 4 variables relating to the number of rooms:<br>
        
        1. <b>Bathrooms:</b> 21 integer values ranging from 0 baths to 42 baths.<br>
        2. <b>Bathrooms_text:</b> 37 string values ranging from 0 baths to 42 baths, including similar values such as <i>'1 bath'</i>, <i>'1 private bath'</i>, and <i>'1 shared bath'</i>.<br>
        3. <b>Bedrooms:</b> 21 integer values ranging from 0 to 41.<br>
        4. <b>Beds:</b> 15 integer values ranging from 0 to 29.<br>

        <b>Missing Values:</b><br>
        • 32.7% of the values for <i>'Bathrooms'</i> are missing, compared to only 0.1% in <i>'Bathrooms_text'</i>.<br>
        • 7.8% of <i>'Bedrooms'</i> values are missing.<br>
        • 32.9% of <i>'Beds'</i> values are missing.<br>
        
        As <i>'Bathrooms_text'</i> had significantly fewer missing values, we chose to use it instead, converting its values to a numerical format.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section 5.3: Number of Reviews and Score Rating
    st.subheader("📂Number of Reviews and Score Rating📊⭐")
    st.markdown(
        """
        <div class="justified-text">
        13 variables in the dataset relate to reviews. We focused on two primary variables:<br>
        
        1. <b>number_of_reviews:</b> 592 integer values ranging from 0 to 3,295, representing the total number of reviews a listing has received.<br>
        2. <b>review_scores_rating:</b> 184 float values ranging from 0.00 to 5.00, indicating the overall rating score based on guest reviews.<br>

        <b>Missing Values:</b><br>
        • <i>'number_of_reviews'</i> has zero missing values.<br>
        • <i>'review_scores_rating'</i> has 28.4% missing values.<br>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section 5.4: Location Data
    st.subheader("📂Location 🏛️🗼")
    st.markdown(
        """
        <div class="justified-text">
        To test the proximity of listings to major tourism sites, we analyzed the location variables:<br>
        
        1. <b>latitude:</b> Latitude of the listing's location.<br>
        2. <b>longitude:</b> Longitude of the listing's location.<br>

        <b>Missing Values:</b> Zero missing values for both <i>'latitude'</i> and <i>'longitude'</i>.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[2]:
    st.header("Data Cleaning & Preparation")



    # Section 6.1: Cleaning the Price Column
    st.subheader("💰Price Column ")
    st.markdown(
        """
        <div class="justified-text">
        To ensure a complete dataset and avoid potential biases in analysis, the <i>price</i> column was cleaned by filling missing values using the mode method. 
        The most frequent price value in the dataset was calculated using pandas' <code>.mode()</code> function, and all missing values in the price column were replaced with this mode. <br><br>

        This approach helped maintain the integrity of the dataset, particularly useful when dealing with categorical or skewed numerical data. 
        After applying this method, the <i>price</i> column contained no missing values, ensuring consistency for subsequent analysis and modeling. 
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section 6.2: Cleaning the Bathroom_text Column
    st.subheader("🚿 Bathroom_text Column")
    st.markdown(
        """
        <div class="justified-text">
        The <i>Bathroom_text</i> column originally contained text-based categorical values, such as:<br><br>

        • "1 bath", <br> • "2 shared baths", <br> • "1 private bath"

        To facilitate quantitative analysis, these values were converted into numerical format by extracting the integer component while preserving the original meaning. 
        For example:<br>

        • "1 bath" → 1 <br>
        • "2 shared baths" → 2 <br>

        To address missing values, the dataset was segmented based on property type, and missing entries were replaced with the mean bathroom count within each category. 
        
        </div>
        """,
        unsafe_allow_html=True
    )

    # Section 6.3: Handling Missing Values in Beds and Bedrooms Columns
    st.subheader("🛌 Beds and Bedrooms Columns")
    st.markdown(
        """
        <div class="justified-text">
        The <i>beds</i> and <i>bedrooms</i> variables also contained missing values. 
        To mitigate data loss and maintain dataset integrity, missing values were imputed using the mean values calculated for each property type:<br><br>

        • If the average number of bedrooms for <i>"Private Room"</i> listings was 1.1, missing values were replaced with 1. <br>
        • If the average number of beds for <i>"Entire Apartment"</i> listings was 2.8, missing values were adjusted accordingly. <br>

        This approach ensured that imputed values remained representative of the respective property types, reducing potential bias in subsequent analyses. 
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add a new section header and description for the cleaned dataset
    st.subheader("🧹📑 Cleaned and Prepared Data Frame")

    st.markdown(
    """
    <div class="justified-text">
    After thorough data cleaning, imputation of missing values, and preparation processes, 
    the dataset is now fully pre-processed and ready for visualization. This ensures that 
    all analyses and models are based on a consistent, complete, and high-quality dataset, 
    maximizing the reliability of the insights generated. 
    </div>
    """,
    unsafe_allow_html=True
    )

    import pandas as pd

    # Load the cleaned and pre-processed data
    file_path_cleaned = "AirBnB/df_last_encoding_drop.csv"
    df_cleaned = pd.read_csv(file_path_cleaned)

    # Select specific columns to display in the table
    columns_to_display_cleaned = [
        'property_type', 'latitude', 'longitude', 'bathrooms_text',
        'bedrooms', 'beds', 'price', 'number_of_reviews', 'review_scores_rating'
    ]

    # Create a smaller dataframe with the selected columns
    df_cleaned_display = df_cleaned[columns_to_display_cleaned].head(10)  # Display only the first 10 rows

    # Display a smaller header for the table
    st.markdown(
    """
    <h4 style='font-size:16px; color:gray;'>
    Final Airbnb Listings Sample Data
    </h4>
    """,
    unsafe_allow_html=True
    )

    st.dataframe(df_cleaned_display)

    # Display the shape of the full dataframe
    st.markdown(f"**Dataset Shape:** `{df_cleaned.shape}` (rows, columns)")

  

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[3]:
    st.header("Exploratory Data Visualization")

    # Section 7.1: Evaluating the Impact of Review Scores on Pricing Strategy
    st.subheader("📈 Impact of Review Scores on Pricing")

    st.markdown(
    """
    <div class="justified-text">

    To gain deeper insights into the relationship between property pricing and customer satisfaction, 
    we analyzed the correlation between <i>price</i> and <i>review scores rating</i>. <br>
    
    This visualization aimed to determine whether higher prices 💵 are associated with better guest experiences 😃 
    or if more affordable properties can achieve similarly high ratings.📈 <br>
    
    By exploring this relationship, we aimed to identify potential patterns that could influence pricing strategies 
    and enhance our understanding of factors contributing to positive reviews. The findings from this analysis 
    are critical for interpreting market positioning and guiding future decision-making processes.
    </div>
    """,
    unsafe_allow_html=True
    )
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import streamlit as st

    # Load the data
    file_path_cleaned = "AirBnB/df_last_encoding_drop.csv"
    df_final = pd.read_csv(file_path_cleaned)



    # Create a container for the side-by-side plots
    col1, col2 = st.columns(2)

    # Plot 1: Price vs. Review Scores Rating
    with col1:
        
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        sns.scatterplot(
            data=df_final, 
            x='review_scores_rating', 
            y='price', 
            alpha=0.6, 
            color='#FF5A5F', 
            s=70, 
            ax=ax1
        )
        ax1.set_xlabel('Review Scores Rating')
        ax1.set_ylabel('Price [$]')
        ax1.set_title('Price vs. Review Scores Rating')
        ax1.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig1)

    # Plot 2: Number of Reviews vs. Review Scores Rating
    with col2:
        
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sns.scatterplot(
            data=df_final, 
            x='review_scores_rating', 
            y='number_of_reviews', 
            alpha=0.6, 
            color='#00A699', 
            s=70, 
            ax=ax2
        )
        ax2.set_xlabel('Review Scores Rating')
        ax2.set_ylabel('Number of Reviews')
        ax2.set_title('Number of Reviews vs. Review Scores Rating')
        ax2.set_ylim(0, 3500)
        ax2.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig2)

    st.markdown(
        """
        <div class="justified-text">
        The analysis shows that most well-reviewed properties (4-5 stars) are reasonably priced (under $500)  
        and attract a high number of reviews, reflecting strong customer satisfaction.<br><br>

        Luxury properties with high prices do not consistently achieve better ratings, indicating that price alone 
        does not guarantee a superior experience. Well-reviewed listings often receive more guest feedback, 
        but even niche or high-quality properties with fewer reviews can maintain high scores. <br>

        Overall, factors like amenities🛋️, location📍and service quality🌟 significantly influence 
        guest satisfaction beyond just price and review count. 
        </div>
        """,
        unsafe_allow_html=True
    )
    # Section 7.2: Impact of Property Type Categories on Pricing
    st.subheader("🏠 Impact of Property Type Categories on Pricing")

    st.markdown(
        """
        <div class="justified-text">
        As previously described, we categorized property types into <b>"Entire Unit"</b>🏢, <b>"Private Room"</b>🚪, 
        and <b>"Shared Room"</b>🛏️. We began by analyzing how these grouped categories influence pricing. <br><br>
        
        The bar chart below compares average prices across these categories, highlighting which property types 
        command higher prices and supporting strategic pricing decisions.
        </div>
        """,
        unsafe_allow_html=True
    )

    import streamlit as st
    import matplotlib.pyplot as plt
    import pandas as pd
    # Load the cleaned and pre-processed data
    file_path_cleaned = "AirBnB/df_last_encoding.csv"
    df_cleaned = pd.read_csv(file_path_cleaned)

    # Assuming df_filtered contains your data and 'property_type_grouped' is the grouping column
    # Calculate the mean price for each property type group
    grouped_stats = df_cleaned.groupby('property_type_grouped')['price'].mean().reset_index()

    # Visualize the grouped categories with improved aesthetics
    plt.figure(figsize=(15, 6))
    plt.bar(grouped_stats['property_type_grouped'], grouped_stats['price'], alpha=0.8, color=['#FF5A5F', '#00A699', '#FC642D'])

    # Improve title and labels
    plt.xlabel('Grouped Property Type', fontsize=12, labelpad=10)
    plt.ylabel('Average Price [$]', fontsize=12, labelpad=10)
    plt.title('Average Price by Grouped Property Type', fontsize=16)

    # Add gridlines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Customize ticks
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Adjust layout
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())



    st.write(
    """
    <div class="justified-text">
    The chart shows a clear trend: "Entire Unit" accommodations have the highest average price, reflecting premium pricing for full privacy.<br><br>

    "Private Room" options are moderately priced, balancing privacy and affordability, 
    while "Shared Room" accommodations are the most economical, appealing to budget-conscious travelers.

    These insights support strategic pricing decisions by highlighting how property types align with 
    different market segments, from luxury seekers to budget travelers.
    """,
    unsafe_allow_html=True
    )

    # Section 7.3: Impact of Property Type on Pricing
    st.subheader("🏘️ Impact of Property Type on Pricing")

    st.write(
    """
    <div class="justified-text">
    In the previous section, we analyzed average prices across broad property categories 
    ("Entire Unit," "Private Room," "Shared Room"). Now, we delve into <b>specific subcategories </b> 🏘️
    within each group to see if pricing trends remain consistent. <br><br>

    By comparing average and median prices, we aim to identify which property types offer 
    premium or budget-friendly options and gain a deeper understanding of market pricing strategies.
    """,
    unsafe_allow_html=True
    )

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # Load the data
    file_path = "AirBnB/df_last_encoding.csv"
    df_final = pd.read_csv(file_path)

    # Calculate mean and median prices by property type
    price_stats = df_final.groupby('property_type').agg(
        mean=('price', 'mean'),
        median=('price', 'median')
    ).reset_index()

    # Define colors for the three groups
    colors = {
        'Entire': '#FF5A5F',
        'Room/Private Room': '#00A699',
        'Shared Room': '#FC642D'
    }

    # Create a new 'group' column based on property type with only 3 groups
    def categorize_property_type(property_type):
        if 'Entire' in property_type:
            return 'Entire'
        elif 'Room' in property_type or 'Private room' in property_type:
            return 'Room/Private Room'
        elif 'Shared room' in property_type:
            return 'Shared Room'
        else:
            return 'Room/Private Room'

    # Apply the categorization function
    price_stats['group'] = price_stats['property_type'].apply(categorize_property_type)

    # Sort data within each group by mean price in descending order
    price_stats_mean_sorted = price_stats.sort_values(by=['group', 'mean'], ascending=[True, False])

    # Assign colors based on group
    bar_colors_mean = [colors[group] for group in price_stats_mean_sorted['group']]


    fig_mean, ax_mean = plt.subplots(figsize=(12, 6))
    ax_mean.bar(price_stats_mean_sorted['property_type'], price_stats_mean_sorted['mean'],
                color=bar_colors_mean, alpha=0.9)
    ax_mean.set_xticklabels(price_stats_mean_sorted['property_type'], rotation=45, ha='right')
    ax_mean.set_xlabel('Property Type', fontsize=12)
    ax_mean.set_ylabel('Average Price [$]', fontsize=12)
    ax_mean.set_title('Average Price for Each Property Type (Grouped and Sorted by Mean)', fontsize=14)
    ax_mean.grid(axis='y', linestyle='--', alpha=0.7)

    # Set y-axis ticks every 50 units
    ax_mean.set_ylim(0, 500)
    ax_mean.set_yticks(np.arange(0, 501, 50))

    st.pyplot(fig_mean)

    # Sort data within each group by median price in descending order
    price_stats_median_sorted = price_stats.sort_values(by=['group', 'median'], ascending=[True, False])

    # Assign colors based on group
    bar_colors_median = [colors[group] for group in price_stats_median_sorted['group']]


    fig_median, ax_median = plt.subplots(figsize=(12, 6))
    ax_median.bar(price_stats_median_sorted['property_type'], price_stats_median_sorted['median'],
                  color=bar_colors_median, alpha=0.9)
    ax_median.set_xticklabels(price_stats_median_sorted['property_type'], rotation=45, ha='right')
    ax_median.set_xlabel('Property Type', fontsize=12)
    ax_median.set_ylabel('Median Price [$]', fontsize=12)
    ax_median.set_title('Median Price for Each Property Type (Grouped and Sorted by Median)', fontsize=14)
    ax_median.grid(axis='y', linestyle='--', alpha=0.7)

    # Set y-axis ticks every 50 units
    ax_median.set_ylim(0, 500)
    ax_median.set_yticks(np.arange(0, 501, 50))

    st.pyplot(fig_median)

    st.markdown(
        """
        <div class="justified-text">
        "Entire townhouses" command the highest average prices (>$450), positioning them as a premium choice for luxury travelers, 
        while "Entire rental units" provide a more cost-effective option for those seeking privacy.<br><br>

        In the "Private Room" category, "Boutique hotel rooms" achieve top-tier pricing, offering unique and upscale experiences, 
        whereas "Private rooms in B&Bs" represent a budget-friendly alternative.<br>

        The "Shared Room" segment remains the most economical, with average and median prices below $150, 
        demonstrating stable and predictable pricing within this market.
        </div>
        """,
        unsafe_allow_html=True
    )

    import plotly.express as px
    import pandas as pd
    import numpy as np
    import streamlit as st

    # Load the data
    file_path = "AirBnB/df_last_encoding.csv"
    df_filtered = pd.read_csv(file_path)

    # Check for unique property types in the dataset
    unique_property_types = df_filtered['property_type'].unique()
    print("Unique Property Types in Data:", unique_property_types)

    # Define the custom order of property types including all unique values
    custom_order = [
        'Entire townhouse', 'Entire rental unit', 'Entire condo',
        'Entire serviced apartment', 'Entire loft', 'Room in boutique hotel',
        'Room in hotel', 'Private room in rental unit', 'Private room in condo',
        'Private room in bed and breakfast', 'Private room in home',
        'Shared room in rental unit'
    ]

    # Create a jittered version of 'price' for each property type to avoid overlap in the scatter plot
    df_filtered['jittered_x'] = df_filtered['property_type'].apply(
        lambda x: np.random.normal(loc=0, scale=0.1) + custom_order.index(x) 
        if x in custom_order else np.nan
    )

    # Drop rows with NaN values in 'jittered_x' to avoid errors
    df_filtered = df_filtered.dropna(subset=['jittered_x'])

    # Define the color mapping for each property type using Airbnb colors
    color_mapping = {
        'Entire Unit': '#FF5A5F',  # Airbnb Red
        'Private Room': '#00A699',  # Airbnb Teal
        'Shared Room': '#FFD700',   # Yellow
    }

    # Plotly figure using scatter plot
    fig = px.scatter(
        df_filtered,
        x='jittered_x',
        y='price',
        color='property_type',
        color_discrete_map=color_mapping,
        title="💰 Price Distribution by Property Type (Logarithmic Scale) 📈",
        labels={"x": "Property Type", "y": "Price [$] (log scale)"},
        category_orders={"property_type": custom_order},
        log_y=True,
        opacity=0.6
    )

    # Update layout and axes for better readability
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=np.arange(len(custom_order)),
            ticktext=custom_order,
            tickangle=-45,
            title="Property Type"
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=[10, 50, 100, 200, 500, 1000, 5000, int(max(df_filtered['price']))],
            ticktext=["10", "50", "100", "200", "500", "1k", "5k", f"{int(max(df_filtered['price']))}+"],
            title="Price [$] (log scale)"
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        showlegend=True,
        height=800,
        width=1200
    )

    # Add grid lines and customize marker appearance
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_traces(marker=dict(size=10, line=dict(width=1, color='black')))

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🛌 Impact of Beds, Bedrooms, and Bathrooms on Pricing")

    st.markdown(
        """
        <div class="justified-text">
        To gain a deeper understanding of factors influencing Airbnb pricing, we analyzed the distribution of 
        beds, bedrooms, and bathrooms across different property types. These variables are critical in determining 
        a property's capacity, comfort level, and appeal to various guest segments, ranging from solo travelers to 
        large groups. Evaluating these metrics helps refine pricing strategies and optimize property listings to match market demand. <br><br>
        """,
        unsafe_allow_html=True
    )

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data
    file_path = "AirBnB/df_last_encoding.csv"
    df_filtered = pd.read_csv(file_path)


    parameter = st.selectbox(
        "Select the parameter to analyze price distribution:",
        ("bedrooms", "beds", "bathrooms_text")
    )

    # Create a bar chart based on the selected parameter
    if parameter:
        plt.figure(figsize=(10, 6))

        # Plotting based on the selected parameter
        df_filtered.groupby(parameter)["price"].mean().plot(
            kind="bar",
            color="#FF5A5F" if parameter == "bedrooms" else "#00A699" if parameter == "beds" else "#FC642D",
            alpha=0.7
        )

        plt.title(f"Average Price vs {parameter.capitalize()}", fontsize=16)
        plt.xlabel(parameter.capitalize(), fontsize=14)
        plt.ylabel("Average Price [$]", fontsize=14)
        plt.xticks(fontsize=12, rotation=45)
        plt.yticks(fontsize=14)
        plt.ylim(0, 2000)
        plt.grid(axis='y', color='lightgray', linestyle='--', linewidth=0.7)

        plt.tight_layout()

        # Display the plot in Streamlit
        st.pyplot(plt.gcf())

        # Provide some interpretation based on the selection
        st.markdown(
            f"""
            The chart shows the average price distribution based on the selected parameter: **{parameter.capitalize()}**. 
            This visualization helps identify how different values of {parameter} influence Airbnb pricing. 
            """
        )
    st.markdown(
        """
        <div class="justified-text">
        The number of beds🛏️, bedrooms🛋️, and bathrooms🛀 significantly impacts Airbnb pricing. 
        Maximizing revenue involves increasing bedrooms and offering private bathrooms, 
        while budget listings benefit from shared bathrooms and fewer beds. Luxury properties can command higher prices with multiple bedrooms and en-suite bathrooms. 
        "Entire Home/Apt" listings are generally more expensive due to their larger size and private amenities.<br><br>
        """,
        unsafe_allow_html=True
    )
# Impact of location on the price
    st.subheader("📍 Impact of Location on Pricing")

    st.markdown(
        """
        <div style="text-align: justify;">
        As we noticed earlier, the price of Airbnb properties significantly depends on the type of property, 
        with Entire Units, Private Rooms, and Shared Rooms demonstrating distinct pricing patterns. However, location is another crucial factor influencing accommodation costs in Paris. 
        This section explores how geographic location contributes to price variations, providing insights 
        into the premium areas and budget-friendly neighborhoods within the city. Moreover, proximity to iconic landmarks like the 
        Eiffel Tower🗼, Notre-Dame🏛️, and the Louvre 🎨 can have a significant impact on pricing.
        </div>
        """,
        unsafe_allow_html=True
    )

    import streamlit as st
    import plotly.express as px
    import pandas as pd

    # Load the data
    file_path = "AirBnB/df_last_encoding.csv"
    df_final = pd.read_csv(file_path)

    # Define custom colors for property types
    custom_colors = {
        "Entire Unit": "#FF5A5F",  # Coral Red
        "Private Room": "#00A699",  # Teal
        "Shared Room": "#FC642D"    # Soft Orange
    }

    # Coordinates for landmarks
    landmarks = [
        {"name": "Eiffel Tower", "latitude": 48.8584, "longitude": 2.2945},
        {"name": "Notre-Dame Cathedral", "latitude": 48.8529, "longitude": 2.3500},
        {"name": "Louvre Museum", "latitude": 48.8606, "longitude": 2.3376}
    ]

    # Add landmarks as a new DataFrame
    landmarks_df = pd.DataFrame(landmarks)


    fig = px.scatter_mapbox(
        df_final,
        lat="latitude",
        lon="longitude",
        size="price",
        color="property_type_grouped",
        hover_name="property_type_grouped",
        hover_data={"price": True},
        zoom=12,
        center={"lat": df_final["latitude"].mean(), "lon": df_final["longitude"].mean()},
        mapbox_style="open-street-map",
        title="Bubble Map: Average Price by Property Type",
        color_discrete_map=custom_colors
    )

    # Add custom icons for landmarks
    fig.add_scattermapbox(
        lat=landmarks_df["latitude"],
        lon=landmarks_df["longitude"],
        mode="markers+text",
        marker=dict(
            size=20,
            color="purple",
            symbol="circle",
            opacity=1
        ),
        text=landmarks_df["name"],
        textposition="top center",
        name="Landmarks"
    )

    # Ensure legend interaction and increase figure height
    fig.update_layout(
        legend=dict(
            title="Legend",
            traceorder="normal"
        ),
        height=800
    )
# Disciances catrgories 
    # Display the map in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        <div style="text-align: justify;">
        To assess how location influences accommodation pricing in Paris, we analyzed the average price of properties 
        relative to their distance from three iconic landmarks: <b>Eiffel Tower</b>, 
        <b>Notre-Dame Cathedral</b>, and <b>Louvre Museum</b>. By calculating the distance from each property to these landmarks, we aimed to determine whether proximity to 
        major tourist attractions correlates with higher accommodation costs. The analysis categorized distances into 
        five distinct groups:<br>

        • <b>Below 0.5 km </b><br>
        • <b>0.5-1 km</b><br>
        • <b>1-2 km</b><br>
        • <b>2-3 km</b><br>
        • <b>Above 3 km</b><br>
        </div>
        """,
        unsafe_allow_html=True
    )

# Disciances catrgories 

    import streamlit as st
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    from matplotlib.colors import LinearSegmentedColormap
    import numpy as np

    # Load the data
    file_path = "AirBnB/df_last_encoding.csv"
    df_last_encoding = pd.read_csv(file_path)

    # Define the data for prices based on distance categories to landmarks
    data = {
        'eiffel_tower_distance_category': ['Below 0.5 km', '0.5-1 km', '1-2 km', '2-3 km', 'Above 3 km'],
        'eiffel_prices': [408, 260, 238, 227, 178],

        'notre_dame_distance_category': ['Below 0.5 km', '0.5-1 km', '1-2 km', '2-3 km', 'Above 3 km'],
        'notre_dame_prices': [257, 235, 218, 182, 181],

        'louvre_museum_distance_category': ['Below 0.5 km', '0.5-1 km', '1-2 km', '2-3 km', 'Above 3 km'],
        'louvre_prices': [262, 249, 225, 200, 169]
    }

    df = pd.DataFrame(data)

    # Define the desired category order
    category_order = ['Below 0.5 km', '0.5-1 km', '1-2 km', '2-3 km', 'Above 3 km']

    # Define custom gradients for each landmark
    eiffel_cmap = LinearSegmentedColormap.from_list("eiffel_gradient", ["#FF5A5F", "#FF999B"])
    notre_dame_cmap = LinearSegmentedColormap.from_list("notre_dame_gradient", ["#00A699", "#66D0BB"])
    louvre_cmap = LinearSegmentedColormap.from_list("louvre_gradient", ["#FC642D", "#FDB27A"])

    # Create gradient palettes
    eiffel_gradient = sns.color_palette(eiffel_cmap(np.linspace(0, 1, len(category_order))))
    notre_dame_gradient = sns.color_palette(notre_dame_cmap(np.linspace(0, 1, len(category_order))))
    louvre_gradient = sns.color_palette(louvre_cmap(np.linspace(0, 1, len(category_order))))

    # Prepare the data for visualization
    eiffel_prices = pd.DataFrame({
        'distance': df['eiffel_tower_distance_category'],
        'price': df['eiffel_prices']
    }).reindex(df.index)

    notre_dame_prices = pd.DataFrame({
        'distance': df['notre_dame_distance_category'],
        'price': df['notre_dame_prices']
    }).reindex(df.index)

    louvre_prices = pd.DataFrame({
        'distance': df['louvre_museum_distance_category'],
        'price': df['louvre_prices']
    }).reindex(df.index)

    # Function to add gridlines and set y-axis limits
    def add_gridlines_and_set_ylim(ax, y_max=500):
        ax.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
        ax.set_ylim(0, y_max)
        ax.set_yticks(np.arange(0, y_max + 1, 50))


    landmark = st.selectbox(
        "Select a landmark to view price distribution:",
        ("Eiffel Tower", "Notre-Dame Cathedral", "Louvre Museum")
    )

    # Plot based on the selected landmark
    plt.figure(figsize=(8, 4))

    if landmark == "Eiffel Tower":
        ax = sns.barplot(
            data=eiffel_prices,
            x='distance',
            y='price',
            palette=eiffel_gradient,
            order=category_order,
            alpha=0.9
        )
        plt.title('Average Price by Distance to Eiffel Tower', fontsize=14)
        plt.xlabel('Distance to Eiffel Tower', fontsize=12)

    elif landmark == "Notre-Dame Cathedral":
        ax = sns.barplot(
            data=notre_dame_prices,
            x='distance',
            y='price',
            palette=notre_dame_gradient,
            order=category_order,
            alpha=0.9
        )
        plt.title('Average Price by Distance to Notre-Dame Cathedral', fontsize=14)
        plt.xlabel('Distance to Notre-Dame Cathedral', fontsize=12)

    elif landmark == "Louvre Museum":
        ax = sns.barplot(
            data=louvre_prices,
            x='distance',
            y='price',
            palette=louvre_gradient,
            order=category_order,
            alpha=0.9
        )
        plt.title('Average Price by Distance to Louvre Museum', fontsize=14)
        plt.xlabel('Distance to Louvre Museum', fontsize=12)

    plt.ylabel('Average Price [$]', fontsize=12)
    plt.xticks(rotation=45)
    add_gridlines_and_set_ylim(ax)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())



    st.markdown(
        """
        <div style="text-align: justify;">
        The analysis shows that property prices decrease as the distance from major landmarks increases, 
        with the strongest price premium seen near the <b>Eiffel Tower</b> (up to $400 for properties within 0.5 km). Prices near <b>Notre-Dame</b> and the <b>Louvre</b> also drop with distance but more gradually, 
        with the <b>Eiffel Tower</b> having the most significant impact on pricing.
        </div>
        """,
        unsafe_allow_html=True
    )
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[4]:
    st.header("Data Optimization & Feature Engineering")
 
    st.subheader("🔢 Encoding Categorical Variables")

    st.markdown(
        """
        <div style="text-align: justify;">
        Categorical columns were identified and converted into numerical formats using 
        <code>pd.factorize()</code> and <code>pd.cut</code>, enabling compatibility with 
        machine learning algorithms. This step was crucial for transforming categorical data 
        into a format suitable for predictive modeling. Categorical columns were converted into numerical formats using appropriate encoding techniques: <br><br>

        • Property Types (Grouped) were encoded using One-Hot Encoding, creating binary columns for each category.<br>
        • Distance Categories were encoded with the OrdinalEncoder, assigning ordered values (0 to 4) based on proximity.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )
    import streamlit as st
    import pandas as pd

    # Load the data
    file_path = r"AirBnB/df_last_encoding.csv"
    df_last_encoding = pd.read_csv(file_path)


    # Specify the columns to display
    columns_to_display = [
        'bathrooms_text', 'bedrooms', 'beds',
        'property_type_grouped_Entire Unit',
        'property_type_grouped_Private Room',
        'property_type_grouped_Shared Room',
        'eiffel_tower_distance_category',
        'notre_dame_distance_category',
        'louvre_museum_distance_category'
    ]

    # Filter the dataframe to show only the specified columns
    df_selected_columns = df_last_encoding[columns_to_display]

    # Display the filtered dataframe in Streamlit
    st.dataframe(df_selected_columns.head(10))  # Show the first 10 rows for clarity



    st.subheader("🎯 Filtering the Target Variable (Price)")

    st.markdown(
        """
        <div style="text-align: justify;">
        Initially, extreme price values (up to <b>$25,000</b>) negatively impacted model accuracy. 
        The dataset was refined to include only prices between <b>0 and 200</b>, based on insights from the 
        price distribution analysis. This filtering step helped stabilize model predictions and enhance accuracy.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("⚠️ Handling Anomalous Values (Price = 150)")

    st.markdown(
        """
        <div style="text-align: justify;">
        An overrepresentation of the price value 150, likely a default or placeholder, skewed predictions. These values were removed to improve model performance.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.subheader("📊 Visualizing Price Distribution")

    st.markdown(
        """
        <div style="text-align: justify;">
        A histogram and probability density plot were generated to validate the data cleaning process. 
        The visualization confirmed a balanced price distribution without the artificial spike at 
        the <b>150</b> value, indicating the effectiveness of the preprocessing steps.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Load the data
    file_path = r"AirBnB/df_last_encoding.csv"
    df = pd.read_csv(file_path)


    # Drop all NaN values (quickest method, but not always recommended)
    df = df.dropna()


    # Encode categorical variables
    categorical_columns = df.select_dtypes(include=['object']).columns

    for col in categorical_columns:
        df[col], _ = pd.factorize(df[col])
    

    # Filter out extreme price values above 200
    initial_count = df.shape[0]
    df = df[df['price'] <= 200]
    filtered_count = df.shape[0]


    # Remove all instances where price equals 150
    df = df[df['price'] != 150]


    # Plot the histogram and probability density function for the 'price' column
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], kde=True, color="#FF5A5F")
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Histogram and Probability Density Function of Prices')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())



#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[5]:
    st.header(" Machine Learning Models")


    st.subheader("🎯 Regression Models Evaluation")

    st.markdown(
        """
        <div style="text-align: justify;">
        In this section, we present the machine learning models applied to predict and analyze our target variable, <b>price</b>. 
        We tested five regression models to determine the best-performing model for accurate predictions and robust insights. 
        Based on the evaluation, the <b>Random Forest Regression🌲</b> model showed the highest performance and was selected for predictions in the next step. <br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    from PIL import Image
    import os

    # Define the path to the images folder
    image_folder_path = "C:/Users/eddeg/Desktop/Data analysis course_Streamlit/"

    # Define the available models and corresponding image file names
    model_image_mapping = {
        "Random Forest Regression": "Random Forest Regression.jpg",
        "Ridge Regression": "Ridge Regression.jpg",
        "Linear Regression": "Linear Regression.jpg",
        "Lasso Regression": "Lasso Regression.jpg",
        "Decision Tree": "Decision Tree.jpg"
    }

    # Create a dropdown selection for the models
    selected_model = st.selectbox("Select a model to display its image:", list(model_image_mapping.keys()))



    # Get the corresponding image file path
    image_path = os.path.join(image_folder_path, model_image_mapping[selected_model])

    # Check if the image path exists before displaying the image
    if os.path.exists(image_path):
        # Display the image with a title

        image = Image.open(image_path)
        st.image(image, caption=f"Model: {selected_model}", use_column_width=True)
    else:
        st.error(f"Image file not found for the model: {selected_model}")

    st.write("Machine learning models metrics:")
    # Display the image showing the results
    image_path = "AirBnB/Results.png"
    image = Image.open(image_path)
    st.image(image, caption="Model Performance Comparison: Random Forest Achieved the Best Results", use_column_width=True)

    st.subheader("🎯 Classification Model Evaluation")

    import streamlit as st


    st.markdown(
    """
    <div style="text-align: justify;">
    We also explored a classification approach by categorizing prices into four classes using 
    <code>pd.qcut</code> and testing a <b>Random Forest Classifier</b>. This method allowed us to assess the 
    model's performance on categorical outputs using metrics such as accuracy, precision, recall, and F1 score. 
    The histogram below visualizes property prices segmented into balanced classes (0, 1, 2, 3) using 
    <code>pd.qcut</code>. <br><br>
    </div>
    """,
    unsafe_allow_html=True
    )
# Display the image with the histogram of classified prices
    image_path = "AirBnB/Prices.jpg"
    image = Image.open(image_path)
    st.image(image, caption="Histogram of Property Prices Categorized into Classes (0, 1, 2, 3)", use_column_width=True)

    st.markdown(
        """
        <div style="text-align: justify;">
        The confusion matrix, combined with the class distribution, provides insights into the model's accuracy 
        and performance across price categories, highlighting strengths and areas for improvement.
        </div>
        """,
        unsafe_allow_html=True
    )

        
    from PIL import Image


    st.markdown(
        """
        <div style="text-align: justify;">
        The confusion matrix, combined with the class distribution, provides insights into the model's accuracy 
        and performance across price categories, highlighting strengths and areas for improvement. <br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display the confusion matrix image
    image_path = "AirBnB/Confusion matrix.jpg"
    image = Image.open(image_path)
    st.image(image, caption="Confusion Matrix for Price Classification Model", use_column_width=True)


    
    st.markdown(
        """
        <div style="text-align: justify;">
       <br> The classification model showed strong performance with an accuracy of <b>0.88</b>. 
        Precision and recall were well-balanced across most classes, with perfect precision for classes <b>0</b> and <b>3</b>. 
        The high F1-score reflects an effective precision-recall balance. The slightly lower recall in class <b>3</b> (0.75) 
        indicates potential for improvement in capturing all relevant instances. Overall, the model demonstrates reliable 
        and consistent classification performance.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    from PIL import Image
    import streamlit as st

    # Define the path to the image
    image_path = "AirBnB/Accuracy.png"

    # Display the image with a caption
    st.image(image_path, caption="Classification Model Accuracy", use_column_width=True)






#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[6]:
    st.header("Prediction")

    import streamlit as st

    st.markdown("""

For predicting Airbnb prices, we used key variables such as:  

- **Property Features:** *bathrooms_text*, *bedrooms*, *beds*  
- **Property Type Categories:** *Entire Unit*, *Private Room*, *Shared Room*  
- **Proximity to Landmarks:** *eiffel_tower_distance_category*, *notre_dame_distance_category*, *louvre_museum_distance_category*  

The model effectively leveraged these variables to provide accurate price predictions, offering valuable insights into market trends and pricing strategies. <br><br>
""",
        unsafe_allow_html=True
    )

    import streamlit as st
    import pickle
    import numpy as np

    # Load the trained Random Forest Regression model from the pickle file
    model_path = "AirBnB/random_forest_model.pkl"
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    st.subheader("🌴Predict Airbnb Price with Random Forest Regression")

    st.markdown(
        """
        <div style="text-align: justify;">
        Use the sliders and dropdowns below to input property features and get a predicted price using the pre-trained Random Forest model.<br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input features
    bathrooms_text = st.slider("Number of Bathrooms 🛁", min_value=0.0, max_value=10.0, step=0.5)
    bedrooms = st.slider("Number of Bedrooms🛋️", min_value=0, max_value=10, step=1)
    beds = st.slider("Number of Beds 🛏️", min_value=0, max_value=15, step=1)

    property_type = st.selectbox("Property Type 🏘️", ["Entire Unit", "Private Room", "Shared Room"])
    property_type_grouped = {
        "Entire Unit": [1, 0, 0],
        "Private Room": [0, 1, 0],
        "Shared Room": [0, 0, 1]
    }

    eiffel_distance = st.selectbox("Distance to Eiffel Tower🗼", ["Below 0.5 km", "0.5-1 km", "1-2 km", "2-3 km", "Above 3 km"])
    notre_dame_distance = st.selectbox("Distance to Notre-Dame Cathedral 🏛️", ["Below 0.5 km", "0.5-1 km", "1-2 km", "2-3 km", "Above 3 km"])
    louvre_distance = st.selectbox("Distance to Louvre Museum🎨", ["Below 0.5 km", "0.5-1 km", "1-2 km", "2-3 km", "Above 3 km"])

    distance_mapping = {
        "Below 0.5 km": 0,
        "0.5-1 km": 1,
        "1-2 km": 2,
        "2-3 km": 3,
        "Above 3 km": 4
    }

    # Prepare input array for prediction
    input_features = [
        bathrooms_text,
        bedrooms,
        beds,
        *property_type_grouped[property_type],
        distance_mapping[eiffel_distance],
        distance_mapping[notre_dame_distance],
        distance_mapping[louvre_distance]
    ]

    # Predict price
    if st.button("Predict Price"):
        predicted_price = model.predict([input_features])[0]
        st.success(f"Predicted Airbnb Price: ${predicted_price:.2f}")




#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
elif page == pages[7]:
    st.header("🎯 Conclusion")

    st.markdown(
        """
        <div style="text-align: justify;">
        This project aimed to analyze the key factors influencing Airbnb pricing in Paris and develop predictive models to optimize pricing strategies. 
        Through extensive data analysis, we identified that factors such as property type 🏠, number of reviews 📝, review scores ⭐, and proximity to 
        landmarks 🗼 are crucial determinants of accommodation prices. Additionally, attributes like the number of bathrooms 🛁, bedrooms 🛌, and available 
        beds 🛏️ played a notable role, emphasizing the importance of space and comfort for guests.
        <br><br>
        
        The best-performing model was the <b>Random Forest Regression 🌳</b>, with R² values of <b>0.242</b> for the test set, and the lowest 
        <b>MAE</b> (<b>29.177</b>) and <b>RMSE</b> (<b>36.320</b>). This model provided the most accurate pricing predictions, balancing accuracy and error 
        minimization. While regression models like Random Forest provided the best results for predicting continuous price values, the 
        <b>Random Forest Classifier</b> demonstrated strong performance for classification tasks with an accuracy of <b>88.2%</b> and solid metrics 
        across all categories.
        <br>
        
        For Airbnb hosts, our analysis offers valuable insights to optimize pricing strategies. Offering <b>"Entire Unit"</b> accommodations 🏢, 
        maintaining high review scores ⭐, optimizing space (through bathrooms, bedrooms, and beds), and positioning properties near key landmarks 
        like the Eiffel Tower 🗼 are strategies that can enhance occupancy and revenue.
        <br>
        
        While our analysis provided robust insights, future work could explore seasonal pricing trends, the impact of specific amenities on 
        guest satisfaction, or expand the analysis to other cities 🌍. Incorporating more advanced machine learning techniques could further 
        refine predictive accuracy and provide deeper insights into the dynamic short-term rental market.
        </div>
        """,
        unsafe_allow_html=True
    )
