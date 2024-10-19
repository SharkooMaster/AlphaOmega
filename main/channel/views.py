from django.conf import settings
from django.shortcuts import get_object_or_404, render
from googleapiclient.discovery import build

from channel.models import Channel

# Create your views here.

def main_page(request,title):
    channel = get_object_or_404(Channel,title=title)
    youtube = build('youtube', 'v3', developerKey=settings.YT_API_KEY)

    # Request channel information
    request = youtube.channels().list(
        part='snippet,statistics,contentDetails',  # You can add more parts if needed
        id=channel.channel_id  # Use the channel ID to identify the channel
    )

    # Execute the request
    response = request.execute()

    channel.description = response['items']['snippet']['description']
    channel.subscriber_count = int(response['items']['statistics']['subscriberCount'])
    channel.views_count = int(response['items']['statistics']['viewCount'])
    channel.save()

    print(response)
    return render(request,"channel/channel.html",{"channel":channel})
