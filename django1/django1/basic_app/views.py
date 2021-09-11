from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserInfo
from .forms import UserForm, UserInfoForm

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

