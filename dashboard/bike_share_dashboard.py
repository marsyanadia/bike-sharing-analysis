import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("bike-sharing-analysis/dashboard/clean_bike_share_data.csv")

# Set page configuration
st.set_page_config(
    page_title="Bike Rental Analysis",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar title
with st.sidebar:
    st.title('🚲 Bike Rental Analysis')
    st.write("#### Nama: Deswita Marsya Nadia \n #### Email: deswitamarsyan@gmail.com \n #### ID Dicoding: marsyanadia")

# Select relevant columns
seasonal_data = df[['season', 'casual', 'registered', 'count']]
yearly_data = df[['year', 'count']]

# Group by and calculate sum
seasonal_sum = seasonal_data.groupby('season').sum()
yearly_trends = yearly_data.groupby('year').sum()

# Define seasons and year
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonal_sum.index = seasons

years = ['2011', '2012']
yearly_trends.index = years



# Create two columns for layout
col1, col2 = st.columns(2)

# Display the DataFrame in the first column
with col1:


    st.title('Seasonal Data')
    st.write("## Number of Bike Rentals by Season")
    st.write(seasonal_sum)
    # Plot bar chart
    st.bar_chart(seasonal_sum)

    st.title('Yearly Data')
    st.write("## Yearly Trends of Bike Rentals (2011 vs 2012)")
    st.write(yearly_trends)
    # Plot bar chart
    st.bar_chart(yearly_trends)

# Calculate total rentals and proportions for each season
total_rentals = seasonal_sum['count'].sum()
proportions = seasonal_sum['count'] / total_rentals

# Calculate growth percentage for yearly data
yearly_trends['growth_percentage'] = yearly_trends['count'].pct_change() * 100 


# Create Plotly pie chart in the second column
with col2:
    st.write('## Percentage of Bike Rentals by Season')
    # Create Plotly pie chart
    fig = px.pie(
        values=proportions,
        names=seasonal_sum.index,
        labels={'season': 'Season', 'value': 'Percentage'},
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.3  # Adjust the size of the hole in the middle of the pie chart
    )

    # Show the Plotly chart in Streamlit app
    st.plotly_chart(fig)

    st.write("Secara keseluruhan, pada musim apa penyewaan sepeda banyak diminati?")
    st.write("Dari diagram di atas dapat disimpulkan bahwa terdapat perbedaan jumlah peminjaman sepeda di setiap musim. Diagram tersebut menunjukkan bahwa secara keseluruhan, peminjaman sepeda berada di puncaknya pada saat musim gugur (32.2%), dan presentase peminjaman terendahnya ada di musim semi (14.3%).")

    st.write('## Yearly Growth Percentage')
    # Plot bar chart
    st.bar_chart(yearly_trends['growth_percentage'])

    st.write("Apakah ada peningkatan jumlah peminjam dari tahun ke tahun?")
    st.write("Dari diagram di atas dapat disimpulkan bahwa dari tahun 2011 ke 2012 (1 tahun), terdapat kenaikan jumlah peminjam sepeda. Peminjam tersebut sudah termasuk peminjam casual dan registered. Jadi, dari diagram tersebut didapatkan informasi bahwa jumlah peminjaman sepeda meningkat sebanyak lebih dari 60% dalam kurun waktu satu tahun.")



