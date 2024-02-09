import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to load data from CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Function to display top videos by a metric
def display_top_videos(df, metric, n=7):
    st.subheader(f"Top {n} Videos by {metric}")
    top_videos = df.sort_values(by=metric, ascending=False).head(n)
    st.dataframe(top_videos[['Title', metric]])

# Function to display distribution as pie chart
def display_pie_chart(data, metric):
    st.subheader(f"{metric} Distribution")
    distribution = data[metric].sum()
    st.plotly_chart(px.pie(values=[distribution], names=[metric], title=f"{metric} Distribution"))

# Function to display trend as line chart
def display_line_chart(data, metric):
    st.subheader(f"Trend of {metric} Over Time")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data[metric], mode='lines+markers'))
    fig.update_layout(title=f"{metric} Over Time", xaxis_title='Date', yaxis_title=metric)
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

        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Display top videos by views, likes, and comments
        display_top_videos(df, 'Views')
        display_top_videos(df, 'Likes')
        display_top_videos(df, 'Comments')

        # Display distribution of views, likes, and comments
        st.markdown("---")
        display_pie_chart(df, 'Views')
        display_pie_chart(df, 'Likes')
        display_pie_chart(df, 'Comments')

        # Display trend of views, likes, and comments over time
        st.markdown("---")
        display_line_chart(df, 'Views')
        display_line_chart(df, 'Likes')
        display_line_chart(df, 'Comments')

if __name__ == "__main__":
    main()
