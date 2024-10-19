from django.conf import settings
from django.shortcuts import get_object_or_404, render
from googleapiclient.discovery import build

from channel.models import Channel
import json

# Create your views here.

def channel_videos(playlist_id,amount):
    youtube = build('youtube', 'v3', developerKey=settings.YT_API_KEY)
    yt_request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=amount  # You can specify how many results you want, max 50 per request
    )
    response = yt_request.execute()
    from page.views import format_videos

    print(response)
    return format_videos(response)

def get_videos(request,channel_id,amount):
    channel:Channel = get_object_or_404(Channel,channel_id=channel_id)
    return render(request,"channel/videos.html",{'videos':channel_videos(channel.playlist_id,amount)})


def main_page(request,channel_id):

    channel :Channel = get_object_or_404(Channel,channel_id=channel_id)

    ## TODO Only refresh some time maybe?

    youtube = build('youtube', 'v3', developerKey=settings.YT_API_KEY)
    # Request channel information
    yt_request = youtube.channels().list(
        part='snippet,statistics,contentDetails',  # You can add more parts if needed
        id=channel.channel_id  # Use the channel ID to identify the channel
    )

    # Execute the request
    response = yt_request.execute()

    channel.description = response['items'][0]['snippet']['description']
    channel.subscriber_count = int(response['items'][0]['statistics']['subscriberCount'])
    channel.views_count = int(response['items'][0]['statistics']['viewCount'])
    channel.profile_high = response['items'][0]['snippet']['thumbnails']['high']['url']
    channel.profile_medium = response['items'][0]['snippet']['thumbnails']['medium']['url']
    channel.profile_small = response['items'][0]['snippet']['thumbnails']['default']['url']
    channel.playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    channel.save()

    return render(request,"channel/channel.html",{'channel':channel})
