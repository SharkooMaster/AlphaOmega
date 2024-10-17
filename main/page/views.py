from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from page.models import Video
import json

from googleapiclient.discovery import build

def index(request):
	getRandomVideos()
	video = Video.objects.order_by('?')[:40]

	return render(request, "page/home.html", {'videos': video, "vert": False})

def search(request):
	_term = request.GET.get('term', 'christ is king')
	print(_term)
	response = performSearch(_term)

	videos = []
	for item in response['items']:
		if 'contentDetails' in item and not item['contentDetails'].get('embeddable', True):
			continue

		video_id = item['id']['videoId']

		thumbnails = item['snippet']['thumbnails']
		default_thumbnail = thumbnails['default']['url'] if 'default' in thumbnails else None
		medium_thumbnail = thumbnails['medium']['url'] if 'medium' in thumbnails else None
		high_thumbnail = thumbnails['high']['url'] if 'high' in thumbnails else None

		video_data = {
			'title': item['snippet']['title'],
			'video_id': video_id,
			'description': item['snippet']['description'],
			'thumbnail': medium_thumbnail,  # Higher resolution thumbnail
			'embed_url': f"https://www.youtube.com/embed/{video_id}"
		}
		videos.append(video_data)
	return render(request, "page/home.html", {"videos": videos, "vert": True})

def performSearch(_term, _maxRes = 50):
	youtube = build('youtube', 'v3', developerKey=settings.YT_API_KEY)
	request = youtube.search().list(
		q=_term,
		part="snippet",
		type="video",
		maxResults=_maxRes
	)
	return request.execute()

def getRandomVideos():
	response = performSearch(settings.YT_SEARCH_TERM)

	for item in response['items']:
		if 'contentDetails' in item and not item['contentDetails'].get('embeddable', True):
			continue

		video_id = item['id']['videoId']

		thumbnails = item['snippet']['thumbnails']
		default_thumbnail = thumbnails['default']['url'] if 'default' in thumbnails else None
		medium_thumbnail = thumbnails['medium']['url'] if 'medium' in thumbnails else None
		high_thumbnail = thumbnails['high']['url'] if 'high' in thumbnails else None

		video_data = {
			'title': item['snippet']['title'],
			'videoId': video_id,
			'description': item['snippet']['description'],
			'thumbnail': medium_thumbnail,  # Higher resolution thumbnail
			'embed_url': f"https://www.youtube.com/embed/{video_id}"
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

def showVideo(request, video_id):
	embed_url = f"https://www.youtube.com/embed/{video_id}"
	videos = Video.objects.order_by('?')[:20]
	return render(request, "page/video.html", {'video': Video.objects.get(video_id=video_id), 'embed_url': embed_url, 'recommended': videos})
