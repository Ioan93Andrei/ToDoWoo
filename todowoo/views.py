from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

def home(request):
  return render(request, 'todowoo/home.html')

def signupuser(request)
  return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm()})

