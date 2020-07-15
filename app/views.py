"""suppose we want to know the type of request at any place,we just need to
type(print(request.method())) so we will get to know whether it is a GET request
or a POST request"""
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from .models import *
# Create your views here.
""" def signup
after making changes to signup.html by adding enctype,csrf_token,name to each
field we come here to create a view Whenever we are submitting a form,a POST req
is Generated and data that comes along with it is stored in (request.POST),we
sent a POST request so we need to check whether request is post or not ,if it
is then we take first name using"first_name = request.POST.get('first_name')"
first_name in brackets is the one that we have assigned as name in signup.html
page of templates folder in app||
for files whenever we r uploading any file using the form the way we access the
file is request.FILES['image'] this image is the name that we have assigned to
image field in signup.html||
initially its always the GET request so 1st we r loading the page the req is GET
and it directly renders the signup.html which we have written at the end of this
function bcz if it doesn't go inside the signup def then it returns rendering the
same signup page ,conclusion on reloading GET request id generated and on
clicking submit button a POST request is generated (so we need to fill the form
details  and then click on submit button which then again refereshes the page by
returning signup.hyml page).||
In django whenever u have to use User model for the authentication or login of
user ,it happens through username and password feature but here we r using email
-address instead of usename so we need to make username=email-id and 1more thing
we can't give passwd directly so we have to hash it ,,for password we can't
write directly it needs to be hashed so for hashing there is a function called
make_password which hashes the password and we store it in objected.password for
we need to import make_password from hashers||
after making changes make sure u save it.||
we need to import all the models so that we can use models like userinfo as in
here required,all the fields or data should be of this particular user we have
created right now above using inbilt User model.this will create userinfo object
as well it will link to that particular user we have created
"""


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        image = request.FILES['image']
        user = User.objects.create(username = email , first_name = first_name ,last_name = last_name , email=email)
        print("User object is created")
        user.password = make_password(password)
        user.save()
        print("Password Changed Successfully")
        userinfo.objects.create(user = user , Birthday = birthday , Gender = gender , profile_pic = image)
        print("UserInfo is Added")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
    return render(request,'signup.html',)

#authenticate is the inbuilt function of django for which we need to import firstname
# from django.contrib.auth import authenticate as well as login and logout
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username ,password=password)
        if user:
            login(request,user)
            print("User has logged in")
            return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
        else:
            print("Wrong password")
            return HttpResponse("Somebody Tried to login but he failed")
    return render(request,'signup.html',)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:signup'))


#pk is the primary key that we see in the url as 127.0.0.1:8000/home/1 something
#like this so 1 is pk here through which we can determine the user and his details
#and userinfo details as well by linking both
#(for user details->user = User.objects.get(pk = pk)) and for user info details
#->user_info = userinfo.objects.get(user = user)<-this is for limkimg the user
#info of particular same user and we created a dictionary context(predefined by
#django) which containds the data to be passed
def home(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user = user)
    all_posts = Post.objects.all().order_by('-pk')
    all_users = userinfo.objects.all()
    all_comments = []
    for p in all_posts:
        all_comments.append(Comments.objects.filter(post=p).order_by('-pk'))
    context = {
        "user":user,
        "user_info":user_info,
        "all_posts":all_posts,
        "all_users":all_users,
        "all_comments":all_comments,
    }
    return render(request , 'home.html', context)


#we are creating a view which also contains pk to idetify who has posted for
#which we have user and user_info and if the its a POST request then obiously
#we need to post either the text,image or video ,so for image and video its not
#compulsory that we should always select that so we need to handle the error by
#using try and except and then finally we need to post the object and redirect
#it to the home page and in post we should also include the likes and comments
#which needs to be initially zero.

def makepost(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user = user)
    if request.method == 'POST':
        text = request.POST.get('text')
        try:
            post_img = request.FILES['image']
        except:
            post_img = None
        try:
            post_video = request.FILES['video']
        except:
            post_video=None
        Post.objects.create(user=user , user_info = user_info , text = text , image = post_img , video = post_video , l =0 , c=0)
        print("Post Created Successfully")
        return HttpResponseRedirect(reverse('app:home' , args=(user.id,)))


#first two lines are raeding the data in this case the post_id and user_id and
#next two lines r for getting those objects of a particular user then we need to
#check filter the posts and users and check whether that particulr user has liked
#that post r not if yes then decrease the like by one ie unlike the post and
#save it and delete the entry in console else increase the like by one and
#create the entry and save and last return the post likes
def likepost(request):
    post_id = request.GET.get('post_id')
    user_id = request.GET.get('user_id')
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=user_id)
    if likes.objects.filter(post = post).filter(user = user).exists():
        post.l = post.l - 1;
        post.save()
        likes.objects.filter(post=post).filter(user = user).delete()
        return HttpResponse(post.l)
    post.l = post.l + 1
    likes.objects.create(user = user , post = post)
    post.save()
    return HttpResponse(post.l)


#added the post on which the comment is ,who made the comment,the body of the
#comment and since we ned to add the comment we have have made down the post we
#have to use a list for this purpose along with JsonResponse,basicall it passes
#dictionary as an argument but here as we are passing list ans an argumnet to
#Json Response we need to pass safe=False as an argument too.
def comment(request):
    post_id = request.GET.get('post_id')
    user_id = request.GET.get('user_id')
    body = request.GET.get('body')
    post = Post.objects.get(pk=post_id)
    post.c = post.c+ 1;
    post.save()
    user = User.objects.get(pk=user_id)
    c = Comments.objects.create(user=user , post = post , body = body)
    print("Comment object has been created")
    l=[];
    l.append(c.user.first_name)
    l.append(c.user.last_name)
    l.append(c.body)
    l.append(post.c)
    return JsonResponse(l,safe=False)




def profile(request,pk,ppk):
    in_user = User.objects.get(pk=pk)
    in_user_info = userinfo.objects.get(user=in_user)

    view_user = User.objects.get(pk=ppk)
    view_user_info = userinfo.objects.get(user=view_user)

    all_posts = Post.objects.filter(user=view_user).order_by('-pk')
    all_comments = Comments.objects.all().order_by('-pk')

    context = {
        'in_user':in_user,
        'in_user_info':in_user_info,
        'view_user':view_user,
        'view_user_info':view_user_info,
        'all_posts':all_posts,
        'all_comments':all_comments,
    }

    return render(request , 'profile.html', context)


def cover_pic_change(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user=user)
    user_info.cover_pic = request.FILES['cover_picture']
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile' , args=(user.id,user.id,)))

def profile_pic_change(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user=user)
    user_info.profile_pic = request.FILES['profile_img']
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile' , args=(user.id,user.id,)))

def addbio(request,pk):
    user = User.objects.get(pk = pk)
    user_info = userinfo.objects.get(user=user)
    user_info.about = request.POST.get('body')
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile', args = (user.id , user.id)))
