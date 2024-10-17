from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from page.models import Video
import json

from account.models import Account

from googleapiclient.discovery import build

# Create your views here.
def index(request):

	# If no account exists redirect to signin
	try:
		account : Account = get_object_or_404(Account,user=request.user)
	except:
		return redirect("/account/signin")


	# Call the function to get videos
	video = getRandomVideos(account)
	# video = getVideos()
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

def getRandomVideos(account: Account):
	youtube = build('youtube', 'v3', developerKey=settings.YT_API_KEY)

	request = youtube.search().list(
		q=account.home_screen_tags,
		part="snippet",
		type="video",
		maxResults=50
	)

	response = request.execute()

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

		videos.append(video_data)

	return videos

def showVideo(request, video_id):
	embed_url = f"https://www.youtube.com/embed/{video_id}"
	videos = Video.objects.order_by('?')[:20]
	return render(request, "page/video.html", {'video': Video.objects.get(video_id=video_id), 'embed_url': embed_url, 'recommended': videos})
