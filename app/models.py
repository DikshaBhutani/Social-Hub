from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


"""Create your models here.in sql we create table
in django models are created using class timezone.now = current time on website
of django we have different types of fields which we can refer mx_length is a
compulsory parameter in Charfield ,,null=none(in python),establish relationship
btw user and model,has 1-1,many-1,1-many relationships & in profile_pic of
user_info model django creates a folder name profile_pic bz of
(upload_to='profile_pic/') since it is not existing and then we go to
settings.py file to know where is that folder created """


class userinfo(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    Birthday = models.DateField(default = timezone.now)
    Gender = models.CharField(max_length = 10,default = "Male")
    about = models.CharField(max_length = 200, blank = True)
    profile_pic = models.ImageField(upload_to='profile_pic/')
    cover_pic = models.ImageField(upload_to='cover_pic/')

#called automatically whenever userinfo model is called and we want to show our
#firstname or anything else instead of userinfo1
    def __str__(self):
        return self.user.first_name


"""
#we need to create the Post model which ddeals with the many to one relationship
#so for this relationship we have to use ForeignKey and we need to create models
#(tables) for text,image and video and likes and comments as well and don't
#forget to include__str__ to get the name or some uniue related to user on the
#post not as object1 object2 in the admin table """

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_info =  models.ForeignKey(userinfo,on_delete=models.CASCADE)
    text = models.CharField(max_length=400,blank=True)
    image = models.ImageField(upload_to='post-images/',null=True)
    video = models.FileField(upload_to='post-videos/',null=True)
    l = models.IntegerField(default = 0)
    c = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.first_name



"""here we need to create likes model where exists many to one relationship
between user and posts for which we use predifined ForeignKey don't forget to
register the model in admin.y of app folder and make & apply migrations """

class likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)

    def __str__(self):
        return self.user.first_name


"""similarly for comments as in case of likes model ,1 extra thingy is created
 ie the body partwhich contains the text of max 100 characters"""

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name
