from django.shortcuts import render

from django.contrib.admin.options import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from page.models import Video

from account.models import Account
from playlist.models import PlayList

# Create your views here.

def playlist(request,name):
    playlist = get_object_or_404(Account,user=request.user).playlists.filter(title=name)[0]

    return render(request,"playlist/playlist.html",{"playlist":playlist})


def create_new_playlist(request):
    playlist = PlayList(owner=get_object_or_404(Account,user=request.user))
    playlist.save()
    vals = '{"type":"'+request.POST['type']+'"}'
    html = f"""
        <form
         hx-vals='{vals}'

          hx-post='/playlist/settitle/{playlist.pk}/' >
        <input name='title' class='input input-bordered' placeholder='Playlist title' />
        <button  class='btn btn-primary'>Save</button>
        </form>
    """
    return HttpResponse(html)

def get_link(request,pk):
    _playlist = get_object_or_404(PlayList,pk=pk)
    pass



def set_title(request,pk):
    _playlist = get_object_or_404(PlayList,pk=pk)
    _playlist.title= request.POST['title']
    _playlist.save()
    if request.POST['type'] == 'link':
        html = f"<a href='/playlist/{_playlist.title}' class='link'>{_playlist.title}</a>"
        return HttpResponse(html)
    if request.POST['type'] == 'checkbox':
        html = f"""
		<input type="checkbox"
			hx-post="/playlist/addvideo/{playlist.pk}/{video.pk}/"
			hx-target="#model"
			class="checkbox" />
			{_playlist.title}
        """
        return HttpResponse(html)


def get_playlist_popup (request,video):
    return render(request,"playlist/playlistpopup.html",{"account":get_object_or_404(Account,user=request.user),"video":get_object_or_404(Video,pk=video)})

def addvideo(request,playlist,video):
    playlist = get_object_or_404(PlayList,pk=playlist)
    playlist.videos.add(get_object_or_404(Video,pk=video))
    return HttpResponse("")

def removevideo(request,playlist,video):
    playlist = get_object_or_404(PlayList,pk=playlist)
    playlist.videos.remove(get_object_or_404(Video,pk=video))
    return HttpResponse("")
