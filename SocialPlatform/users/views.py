from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from .models import Profile


def login_user(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('users:index')
            else:
                return HttpResponse("Invalid login creds")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

@login_required
def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
        
    else:
        user_form = UserRegistrationForm()
        return render(request, 'users/register.html', {'user_form':user_form})