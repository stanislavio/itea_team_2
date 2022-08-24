from django.contrib import admin

# Register your models here.
from .models import User, TrainingPost, SocialPost
admin.site.register(User)
admin.site.register(TrainingPost)
admin.site.register(SocialPost)
