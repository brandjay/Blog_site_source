from django.urls import path
from . import views

urlpatterns = [

    path('news/', views.display_blog, name='display_blog'),
   # path('list/', views.display_post, name='news'),
#gives path to single page displaying news article 
    path('article/<int:blog_id>/', views.display_article, name='display_article'),

    


    

    
]