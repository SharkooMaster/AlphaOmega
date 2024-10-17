from django.contrib.admin.options import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomSignUpForm
from .forms import CustomLoginForm

from account.models import Account
from page.models import Video

# Create your views here.


def playlist(request,name):
    playlist = get_object_or_404(Account,user=request.user).playlists.filter(title=name)[0]

    return render(request,"account/playlist.html",{"playlist":playlist})

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/account')  # Redirect to the home page or any other page
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    return render(request, 'account/signin.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            account = Account(user=user)
            account.save()
            account.create_watch_later()

            login(request, user)  # Automatically log the user in
            messages.success(request, 'Account created successfully!')
            return redirect("/")  # Redirect to home or any page after sign up
    else:
        form = CustomSignUpForm()

    return render(request, 'account/signup.html', {'form': form})

def addtowatchlater(request, video:int):
    video = get_object_or_404(Video,pk=video)

    account : Account = get_object_or_404(Account,user=request.user)
    play = account.watch_later

    play.videos.add(video)
    play.save()

    return render(request,"account/WatchLaterButton.html",{'remove':True})

def removefromwatchlater(request, video:int):
    video = get_object_or_404(Video,pk=video)

    account : Account = get_object_or_404(Account,user=request.user)
    play = account.watch_later

    play.videos.remove(video)
    play.save()

    response = HttpResponse("")
    response.headers['HX-Trigger'] = "removedfromwatchlater"
    return response
    #return render(request,"account/playlist.html",{"playlist":play})

def settings(request):
    account: Account = get_object_or_404(Account,user=request.user)
    return render(request,"account/settings.html",{'account':account})

def savesettings(request):
    account: Account = get_object_or_404(Account,user=request.user)
    account.home_screen_tags = request.POST['home_screen_tags']
    account.save()
    return HttpResponse("Saved sucessfully")
