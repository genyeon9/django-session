from django.shortcuts import render
from .models import Bookmark

# Create your views here.

def home(request):
    urlList = Bookmark.objects.order_by('-title')
    urlCount = Bookmark.objects.all().count()
    return render(request, 'home.html', {'urlList':urlList, 'urlCount':urlCount})