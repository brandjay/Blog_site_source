from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.display_blog, name='display_blog'),
]