from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# USER PAGE models !
class User(AbstractUser):
    # Default model names: https://www.csestack.org/django-default-user-model-fields/
    short_bio = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='media')
    birthday = models.DateField(null=True, blank=True,)
    phone = models.CharField(max_length=13, null=True, blank=True, unique=True)
    hide_email = models.BooleanField(default=True)
    hide_phone = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


# FRIEND MODELS
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)



class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)



# POST MODELS
class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)
    comment_text = models.TextField(blank=True)
    def __str__(self):
        return self.comment_text[:70]

class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=200)
    post_photo = models.ImageField(blank=True, null=True)
    post_lead = models.CharField(max_length=200, blank=True)
    post_text = models.TextField(blank=True)
    post_is_private = models.BooleanField(blank=True, null=True)
    comments = models.ManyToManyField(Comment)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.post_title[:50]
#END class Post(models.Model):
   

class SocialPost(Post):
    pass


class TrainingPost(Post):
    datetime_started = models.DateTimeField()
    datetime_finished = models.DateTimeField(blank=True, null=True)

class RunTrainingPost(TrainingPost):
    total_km_ran = models.FloatField(blank=True, null = True)

class SwimTrainingPost(TrainingPost):
    total_km_swum = models.FloatField(blank=True, null = True)
    swimming_location = models.CharField(max_length=200, blank=True, null = True)

class HikeTrainingPost(TrainingPost):
    total_km_walked = models.FloatField(blank=True, null = True)
    hike_location = models.CharField(max_length=200, blank=True, null = True)
    max_elevation = models.FloatField(blank=True, null = True)


# Below are classes for future expansion of the functionality
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_descr = models.CharField(max_length=500)


class Reaction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reaction_type = models.IntegerField() #e.g. 1 - smile, 2- frown, 3 - thumb up etc.


