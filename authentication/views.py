from distutils.command.upload import upload
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from WhatsApp.models import Posts
from Videos.models import Uploads
from .forms import CreateUserForm,EditProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
def home(request):
    post=Posts.objects.all().count()
    upload=Uploads.objects.all().count()
    people=User.objects.count()
    return render(request,'index.html',context={'post':post,'upload':upload,'people':people})
def auth_signup(request):
    form=CreateUserForm()
    registered=False
    if request.method=='POST':
        form=CreateUserForm(data=request.POST)
        if form.is_valid():
            user= form.save()
            registered=True
            user_profile = UserProfile(user=user)
            user_profile.save()
            redirect('authlogin')
            
    return render(request,'authentication/signup.html',context={'form':form})

def authlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))

    return render(request, 'authentication/login.html', context={'form':form})
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('authlogin'))
def Profile(request):
    current = UserProfile.objects.get(user=request.user)
    return render(request,'authentication/profile.html',context={'profile':current})
def editprofile(request):
    current = UserProfile.objects.get(user=request.user)
    form = EditProfileForm(instance=current)
    if request.method =="POST":
        form=EditProfileForm(request.POST,request.FILES,instance=current)
        if form.is_valid():
            form.save(commit=True)
            form =EditProfileForm(instance=current)
            return redirect('profile')
    return render(request,'authentication/editprofile.html',context={'form':form,'title':'Edit Profile.social'})
