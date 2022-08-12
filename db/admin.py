from django.contrib import admin

# Register your models here.
from .models import User, TrainingPost
admin.site.register(User)
admin.site.register(TrainingPost)
