from django.shortcuts import render,redirect 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm

def index(request):
    """The home page for Learning Log."""
    return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password = request.POST['password1'])
            login(request, authenticated_user)
            return redirect('users:index')
    else:
        form = UserCreationForm()
    
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:index')  # Replace 'home' with the name of your home view
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('users:login')

