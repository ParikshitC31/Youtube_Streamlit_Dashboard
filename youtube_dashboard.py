import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data from CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Streamlit app UI
def main():
    st.title("YouTube Video Analytics Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data from CSV
        df = load_data(uploaded_file)

        # Sorting the DataFrame by 'Views', 'Likes', and 'Comments'
        df_sorted_by_views = df.sort_values(by='Views', ascending=False)
        df_sorted_by_likes = df.sort_values(by='Likes', ascending=False)
        df_sorted_by_comments = df.sort_values(by='Comments', ascending=False)

        # Top 7 videos with the most views
        top_views = df_sorted_by_views.head(7)
        bottom_views = df_sorted_by_views.tail(7)

        # Top 7 videos with the most likes
        top_likes = df_sorted_by_likes.head(7)
        bottom_likes = df_sorted_by_likes.tail(7)

        # Top 7 videos with the most comments
        top_comments = df_sorted_by_comments.head(7)
        bottom_comments = df_sorted_by_comments.tail(7)

        # Plotting the bar graphs with horizontal bars
        st.write("## Top 7 Videos by Views")
        st.plotly_chart(px.bar(top_views, y='Title', x='Views', 
                               labels={'Title': 'Video Title', 'Views': 'Views'}, orientation='h'))

        st.write("## Bottom 7 Videos by Views")
        st.plotly_chart(px.bar(bottom_views, y='Title', x='Views', 
                                labels={'Title': 'Video Title', 'Views': 'Views'}, orientation='h'))

        st.write("## Top 7 Videos by Likes")
        st.plotly_chart(px.bar(top_likes, y='Title', x='Likes', 
                               labels={'Title': 'Video Title', 'Likes': 'Likes'}, orientation='h'))

        st.write("## Bottom 7 Videos by Likes")
        st.plotly_chart(px.bar(bottom_likes, y='Title', x='Likes', 
                                labels={'Title': 'Video Title', 'Likes': 'Likes'}, orientation='h'))

        st.write("## Top 7 Videos by Comments")
        st.plotly_chart(px.bar(top_comments, y='Title', x='Comments', 
                                labels={'Title': 'Video Title', 'Comments': 'Comments'}, orientation='h'))

        st.write("## Bottom 7 Videos by Comments")
        st.plotly_chart(px.bar(bottom_comments, y='Title', x='Comments', 
                                 labels={'Title': 'Video Title', 'Comments': 'Comments'}, orientation='h'))

if __name__ == "__main__":
    main()
