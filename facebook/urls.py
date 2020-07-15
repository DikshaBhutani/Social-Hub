"""facebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import settings
from django.contrib.staticfiles.urls import static
"""including the __init__.py file in ur folder helps you to know that
 project "app" is a python file or the python project  && if you
 import everything from app then no need to write(path('',views.home,))
 instead we can write the func name directly as path('',home,) """

""" whenever we type the url (127.0.0.1:8000) it will redirect it to urls.py
file of app (in utlpatterns 2nd path)"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]

"""after doing this set up fro image_field is ready"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
