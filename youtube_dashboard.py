import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data from CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Streamlit app UI
def main():
    st.set_page_config(page_title="YouTube Video Analytics Dashboard", page_icon=":movie_camera:", layout="wide")
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

        # Display top and bottom videos by views, likes, and comments
        st.markdown("### Top and Bottom Videos by Views, Likes, and Comments")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Top Videos by Views")
            st.write(top_views[['Title', 'Views']])

            st.subheader("Top Videos by Likes")
            st.write(top_likes[['Title', 'Likes']])

            st.subheader("Top Videos by Comments")
            st.write(top_comments[['Title', 'Comments']])

        with col2:
            st.subheader("Bottom Videos by Views")
            st.write(bottom_views[['Title', 'Views']])

            st.subheader("Bottom Videos by Likes")
            st.write(bottom_likes[['Title', 'Likes']])

            st.subheader("Bottom Videos by Comments")
            st.write(bottom_comments[['Title', 'Comments']])

        with col3:
            st.subheader("Top Videos by Views (Bar Chart)")
            st.plotly_chart(px.bar(top_views, y='Title', x='Views', 
                                   labels={'Title': 'Video Title', 'Views': 'Views'}, orientation='h'))

            st.subheader("Top Videos by Likes (Bar Chart)")
            st.plotly_chart(px.bar(top_likes, y='Title', x='Likes', 
                                   labels={'Title': 'Video Title', 'Likes': 'Likes'}, orientation='h'))

            st.subheader("Top Videos by Comments (Bar Chart)")
            st.plotly_chart(px.bar(top_comments, y='Title', x='Comments', 
                                   labels={'Title': 'Video Title', 'Comments': 'Comments'}, orientation='h'))

        # Pie chart showing distribution of views, likes, and comments
        st.markdown("### Distribution of Views, Likes, and Comments")
        col4, col5, col6 = st.columns(3)

        with col4:
            st.subheader("Views Distribution")
            views_distribution = df['Views'].sum()
            st.plotly_chart(px.pie(values=[views_distribution], names=["Views"], title="Views Distribution"))

        with col5:
            st.subheader("Likes Distribution")
            likes_distribution = df['Likes'].sum()
            st.plotly_chart(px.pie(values=[likes_distribution], names=["Likes"], title="Likes Distribution"))

        with col6:
            st.subheader("Comments Distribution")
            comments_distribution = df['Comments'].sum()
            st.plotly_chart(px.pie(values=[comments_distribution], names=["Comments"], title="Comments Distribution"))

if __name__ == "__main__":
    main()
