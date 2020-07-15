"""after updating settings.py with media urls and urls.py of facebook with
urlpatterns along withing including the urls for static files we import the
required details ie admin and register the user_info"""
from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(userinfo)
admin.site.register(Post)
admin.site.register(likes)
admin.site.register(Comments)
