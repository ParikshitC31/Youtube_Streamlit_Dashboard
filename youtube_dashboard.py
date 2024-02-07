import streamlit as st
import pandas as pd

# Function to load data from CSV file
def load_data(csv_file):
    data = pd.read_csv('video_metrics.csv')
    return data

# Streamlit app UI
def main():
    st.title("YouTube Video Data Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data from CSV
        data = load_data(uploaded_file)

        st.write("### Sample Data:")
        st.write(data.head())

        st.write("### Data Summary:")
        st.write(data.describe())

        # Display basic statistics
        st.write("### Basic Statistics:")
        st.write(f"Total videos: {len(data)}")
        st.write(f"Total views: {data['Views'].sum()}")

        # Display a bar chart of Views per Title
        st.write("### Views per Title:")
        views_per_title = data.groupby('Title')['Views'].sum().sort_values(ascending=False)
        st.bar_chart(views_per_title)

        # Display a scatter plot of Views vs Likes
        st.write("### Views vs Likes:")
        st.scatter_chart(data[['Views', 'Likes']])

        # Display a scatter plot of Views vs Dislikes
        st.write("### Views vs Dislikes:")
        st.scatter_chart(data[['Views', 'Dislikes']])

        # Display a scatter plot of Views vs Comments
        st.write("### Views vs Comments:")
        st.scatter_chart(data[['Views', 'Comments']])

if __name__ == "__main__":
    main()
