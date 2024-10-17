from django.contrib.admin.options import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import CustomSignUpForm
from .forms import CustomLoginForm

from account.models import Account

# Create your views here.

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
            login(request, user)  # Automatically log the user in
            messages.success(request, 'Account created successfully!')
            return redirect("/")  # Redirect to home or any page after sign up
    else:
        form = CustomSignUpForm()

    return render(request, 'account/signup.html', {'form': form})
