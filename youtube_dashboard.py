import streamlit as st
import duckdb
import pandas as pd

# Connect to DuckDB
conn = duckdb.connect(database='video_metrics.db')

# Run SQL queries to retrieve the top 10 videos by views, likes, dislikes, and comments
top_10_views = conn.execute("SELECT * FROM video_metrics ORDER BY Views DESC LIMIT 10").fetchdf()
top_10_likes = conn.execute("SELECT * FROM video_metrics ORDER BY Likes DESC LIMIT 10").fetchdf()
top_10_dislikes = conn.execute("SELECT * FROM video_metrics ORDER BY Dislikes DESC LIMIT 10").fetchdf()
top_10_comments = conn.execute("SELECT * FROM video_metrics ORDER BY Comments DESC LIMIT 10").fetchdf()
recent_10_videos = conn.execute("SELECT * FROM video_metrics ORDER BY \"Upload date\" DESC LIMIT 10").fetchdf()

# Close the connection
conn.close()

# Streamlit app UI
def main():
    st.title("YouTube Video Analytics Dashboard")

    st.write("## Top 10 Videos by Views")
    st.write(top_10_views)

    st.write("## Top 10 Videos by Likes")
    st.write(top_10_likes)

    st.write("## Top 10 Videos by Dislikes")
    st.write(top_10_dislikes)

    st.write("## Top 10 Videos by Comments")
    st.write(top_10_comments)

    st.write("## Recent 10 Videos Uploaded")
    st.write(recent_10_videos)

if __name__ == "__main__":
    main()
