"""1.(from django.urls import path) using this we r going to create different
sites & (from . import views) we need to import views.py file also bcz we need
to send the control from here to views.py file and as they r in the same folder
we r using from . import views
2.then we willl make urlpatterns to make paths
3.when it finds blank after main url of server it initially comes to url.py file
of the root folder ie facebook where when it finds and matches with the blank
which has an action of redirecting it to urls.py file of the app which then
matches with the particular url suppode for signup page (we want that while
loading the server we should directly come to signup page so on finding or
matching withe blank bcz after server url nothing is wriiten ie blank so we
need to redirect it to views.py file)redirects to signup page as it is going to
views.signup and similarly for the rest
suppose it is unable to match with any url it will display age not found""" 
from django.urls import path
from . import views

app_name = "app"


urlpatterns = [
path('',views.signup,name="signup"),
path('user_login/',views.user_login,name="login"),
path('user_logout/',views.user_logout,name="user_logout"),
path('home/<int:pk>/',views.home,name="home"),
path('makepost/<int:pk>',views.makepost,name="makepost"),
path('likepost/',views.likepost,name="likepost"),
path('comment/',views.comment,name="comment"),
path('profile/<int:pk>/<int:ppk>/',views.profile,name="profile"),
path('cover_pic_change/<int:pk>/',views.cover_pic_change,name="cover_pic_change"),
path('profile_pic_change/<int:pk>/',views.profile_pic_change , name="profile_pic_change"),
path('addbio/<int:pk>/',views.addbio,name="addbio"),
]
