import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
#def news(request):
 #   return HttpResponse('Welcome to News')

def display_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'news/news.html', {'blogs': blogs})
