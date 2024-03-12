from youtube_backend.celery import app
from .models import Video
from datetime import datetime, timedelta
from dotenv import load_dotenv 
import os
from pathlib import Path
import requests

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

SEARCH_API_BASE_URL="https://www.googleapis.com/youtube/v3/search?"
YOUTUBE_API_KEY=os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_KEY_2=os.getenv('YOUTUBE_API_KEY_2')
SEARCH_API_PREFIX=f"{SEARCH_API_BASE_URL}key={YOUTUBE_API_KEY}&type=video&order=date&publishedAfter="
SEARCH_API_PREFIX_2=f"{SEARCH_API_BASE_URL}key={YOUTUBE_API_KEY_2}&type=video&order=date&publishedAfter="

FETCH_API_BASE_URL="https://www.googleapis.com/youtube/v3/videos?id={id}&key={API_KEY}&part=snippet,contentDetails,statistics,status"

def fetch_video_ids():
    today = datetime.today()
    yesterday = today - timedelta(days=7)
    # seconds=10 days=7
    date_time = yesterday.strftime('%Y-%m-%dT%H:%M:%SZ')
    SEARCH_API_ENDPOINT = SEARCH_API_PREFIX + date_time

    try:
        search_data = requests.get(SEARCH_API_ENDPOINT)
    except:
        SEARCH_API_ENDPOINT_2 = SEARCH_API_PREFIX_2 + date_time
        search_data = requests.get(SEARCH_API_ENDPOINT_2)

    search_data_json = search_data.json()
    items = search_data_json["items"]
    ids = list(map(lambda id: id["id"]["videoId"], items))
    return ids

def saveVideoInfoIfNotExists(ids):

    for id in ids:
        try:
            obj = Video.objects.get(id=id)
        except Video.DoesNotExist:
            try:
               videos_data = requests.get(FETCH_API_BASE_URL.format(id=id, API_KEY=YOUTUBE_API_KEY))
            except:
               videos_data = requests.get(FETCH_API_BASE_URL.format(id=id, API_KEY=YOUTUBE_API_KEY_2))
            videos_data_json = videos_data.json()
            item = videos_data_json['items'][0]
            thumbnails = item['snippet']['thumbnails']
            obj = Video(
                id = id,
                title=item['snippet']['title'],
                description=item['snippet']['description'],
                publishing_date=item['snippet']['publishedAt'],
                thumbnail_urls=f"{thumbnails['default']['url']},{thumbnails['medium']['url']},{thumbnails['high']['url']}",
                view_count=item['statistics']['viewCount'],
                duration=item['contentDetails']['duration'],
            )
            obj.save()

@app.task
def task_one():
    ids = fetch_video_ids()
    saveVideoInfoIfNotExists(ids)
    return "task_one executed"
