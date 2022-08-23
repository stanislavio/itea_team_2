from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    short_bio = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True)


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=200)
    post_photo = models.ImageField(blank=True, null=True)
    post_lead = models.CharField(max_length=200, blank=True)
    post_text = models.TextField(blank=True)
    post_is_private = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True
    


class SocialPost(Post):
    pass

class TrainingPost(Post):
    datetime_started = models.DateTimeField()
    datetime_finished = models.DateTimeField(blank=True, null=True)


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_text = models.TextField(blank=True)


#Below are classes for future expansion of the functionality
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_descr = models.CharField(max_length=500)

class Payment(models.Model):
    pass

class Reaction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reaction_type = models.IntegerField() #e.g. 1 - smile, 2- frown, 3 - thumb up etc.

