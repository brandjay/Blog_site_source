# admin.py
from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_content', 'blog_date', 'display_image')

    def display_image(self, obj):
        return obj.blog_image.url if obj.blog_image else ''
    display_image.short_description = 'Image'
