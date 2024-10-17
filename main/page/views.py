from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from page.models import Video
import json

from googleapiclient.discovery import build

# Create your views here.
def index(request):
	# Call the function to get videos
	# video = getRandomVideos()
	video = getVideos()
	# Pass the list of videos in a dictionary with the key 'videos'
	return render(request, "page/home.html", {'videos': video})

def getVideos():
	arr = Video.objects.all()
		
	videos = []
	for item in arr:
		video_id = item.video_id
		embed_url = f"https://www.youtube.com/embed/{video_id}"
		video_data = {
			'title': item.title,
			'videoId': video_id,
			'description': item.description,
			'thumbnail': item.thumbnail,
			'embed_url': embed_url
		}
		videos.append(video_data)
	return videos

def getRandomVideos():
	return Video.objects.all()
	youtube = build('youtube', 'v3', developerKey=settings.YT_API_KEY)

	request = youtube.search().list(
		q=settings.YT_SEARCH_TERM,
		part="snippet",
		type="video",
		maxResults=100
	)

	response = request.execute()

	videos = []
	for item in response['items']:
		video_id = item['id']['videoId']
		embed_url = f"https://www.youtube.com/embed/{video_id}"
		video_data = {
			'title': item['snippet']['title'],
			'videoId': video_id,
			'description': item['snippet']['description'],
			'thumbnail': item['snippet']['thumbnails']['default']['url'],
			'embed_url': embed_url  # Embeddable URL for iframe
		}
		
		# Store the video in the database
		video, created = Video.objects.get_or_create(
			video_id=video_data['videoId'],
			defaults={
				'title': video_data['title'],
				'description': video_data['description'],
				'thumbnail': video_data['thumbnail']
			}
		)

		videos.append(video_data)

	return videos

def showVideo(request, video_id):
	embed_url = f"https://www.youtube.com/embed/{video_id}"
	return render(request, "page/video.html", {'video': Video.objects.get(video_id=video_id), 'embed_url': embed_url})
