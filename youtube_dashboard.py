import streamlit as st
import pandas as pd

# Function to load data from CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Streamlit app UI
def main():
    st.title("YouTube Video Data Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data from CSV
        data = load_data(uploaded_file)

        # Query input fields
        query_title = st.text_input("Enter video title:")
        query_min_views = st.number_input("Enter minimum views:", min_value=0)
        query_min_likes = st.number_input("Enter minimum likes:", min_value=0)
        query_min_dislikes = st.number_input("Enter minimum dislikes:", min_value=0)

        # Filter data based on query inputs
        filtered_data = data[
            (data['Title'].str.contains(query_title, case=False)) &
            (data['Views'] >= query_min_views) &
            (data['Likes'] >= query_min_likes) &
            (data['Dislikes'] >= query_min_dislikes)
        ]

        # Display filtered data
        st.write("### Filtered Data:")
        st.write(filtered_data)

        # Create pie chart of views distribution
        views_distribution = filtered_data['Views'].value_counts()
        st.write("### Views Distribution:")
        st.write(views_distribution)

        # Create line chart of likes vs dislikes
        st.write("### Likes vs Dislikes:")
        st.line_chart(filtered_data[['Likes', 'Dislikes']])

if __name__ == "__main__":
    main()
