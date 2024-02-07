from googleapiclient.discovery import build
from prettytable import PrettyTable

# YouTube API key
yt_key_api = 'AIzaSyDnGfIMQEmRnLmSimSvkr67EAJTzDUl77U'
channel_username = 'NarendraModi'  # Replace with the actual channel username

# Build YouTube API service
youtube = build('youtube', 'v3', developerKey=yt_key_api)

# Function to get metrics for a single video
def get_single_video_metrics(video_id):
    request = youtube.videos().list(part='snippet,statistics', id=video_id)
    response = request.execute()

    # Extract relevant metrics
    if 'items' in response and len(response['items']) > 0:
        video_info = response['items'][0]
        return {
            'video_id': video_id,
            'title': video_info['snippet']['title'],
            'views': int(video_info['statistics'].get('viewCount', 0)),
            'likes': int(video_info['statistics'].get('likeCount', 0)),
            'dislikes': int(video_info['statistics'].get('dislikeCount', 0)),
            'comments': int(video_info['statistics'].get('commentCount', 0))
        }
    else:
        return None

# Function to fetch video metrics for all videos uploaded by the channel
def get_video_metrics(channel_username):
    request = youtube.channels().list(part='contentDetails', forUsername=channel_username)
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        request = youtube.playlistItems().list(part='snippet', playlistId=uploads_playlist_id, maxResults=50)
        video_metrics = []

        while request:
            response = request.execute()
            for item in response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_metric = get_single_video_metrics(video_id)
                video_metrics.append(video_metric)
            request = youtube.playlistItems().list_next(request, response)

        return video_metrics
    else:
        return None

# Fetch and print video metrics for all videos uploaded by the channel
video_metrics = get_video_metrics(channel_username)
if video_metrics:
    table = PrettyTable(['Video ID', 'Title', 'Views', 'Likes', 'Dislikes', 'Comments'])
    for metric in video_metrics:
        if metric:
            table.add_row([metric['video_id'], metric['title'], metric['views'], metric['likes'], metric['dislikes'], metric['comments']])
    print(table)
else:
    print("No videos found for the channel.")
