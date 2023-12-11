from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField(blank=True)
    blog_date = models.DateTimeField(auto_now_add=True)
    
    