from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.

# index/backend page
def index(request):
    return render(request, 'backend/pages/index.html')