import http
#from inspect import _Object
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blog


def display_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'news/news.html', {'blogs': blogs})


#article html file is to show the single post as a full page
def display_article(request, blog_id): 
    blog = get_object_or_404(Blog, pk=blog_id) 
    return render(request, 'news/article.html', {'blog': blog})