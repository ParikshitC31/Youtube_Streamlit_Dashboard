import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data from CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Function to display line chart for a metric over time
def display_line_chart(data, metric):
    st.subheader(f"Trend of {metric} Over Time")
    fig = px.line(data, x='Upload Date', y=metric, title=f"{metric} Over Time")
    st.plotly_chart(fig)

# Streamlit app UI
def main():
    st.set_page_config(page_title="YouTube Video Analytics Dashboard", page_icon=":movie_camera:")
    st.title("YouTube Video Analytics Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data from CSV
        df = load_data(uploaded_file)

        # Convert 'Upload Date' column to datetime
        df['Upload Date'] = pd.to_datetime(df['Upload Date'])

        # Display line charts for all metrics over time
        metrics = ['Views', 'Likes', 'Dislikes', 'Comments']
        for metric in metrics:
            display_line_chart(df, metric)

if __name__ == "__main__":
    main()
