from django.contrib import admin
from .models import User, TrainingPost, SocialPost, Comment

admin.site.register(User)
admin.site.register(TrainingPost)
admin.site.register(SocialPost)
admin.site.register(Comment)
