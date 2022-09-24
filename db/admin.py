from django.contrib import admin
<<<<<<< HEAD
from .models import User, TrainingPost, SocialPost, Comment
=======
from .models import User, TrainingPost, SocialPost, Comment, Friend, RunTrainingPost, SwimTrainingPost, HikeTrainingPost
>>>>>>> NewTrainingPostTypes

admin.site.register(User)

admin.site.register(TrainingPost)

admin.site.register(SocialPost)

admin.site.register(Comment)

admin.site.register(Friend)



@admin.register(SwimTrainingPost)
class SwimTrainingPostAdmin(admin.ModelAdmin):

    # list_display = ("author", "post_title", "post_photo", "post_text")
    # https://stackoverflow.com/questions/28275239/make-django-model-field-read-only-or-disable-in-admin-while-saving-the-object-fi
    exclude=("comments",)
    readonly_fields=('post_lead', )

@admin.register(HikeTrainingPost)
class HikeTrainingPostAdmin(admin.ModelAdmin):

    # list_display = ("author", "post_title", "post_photo", "post_text")
    # https://stackoverflow.com/questions/28275239/make-django-model-field-read-only-or-disable-in-admin-while-saving-the-object-fi
    exclude=("comments",)
    readonly_fields=('post_lead', )



@admin.register(RunTrainingPost)
class RunTrainingPostAdmin(admin.ModelAdmin):

    # list_display = ("author", "post_title", "post_photo", "post_text")
    # https://stackoverflow.com/questions/28275239/make-django-model-field-read-only-or-disable-in-admin-while-saving-the-object-fi
    exclude=("comments",)
    readonly_fields=('post_lead', )
 
    # search_fields = ["user__username"]
 
    # inlines = [
    #     ProjectsInLine, TagsInLine
    # ]
 
    # def _projects(self, obj):
    #     return obj.projects.all().count()
 
    # def _tags(self, obj):
    #     return obj.tags.all().count()

