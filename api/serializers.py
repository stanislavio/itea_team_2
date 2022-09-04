from rest_framework import serializers
from db.models import User

from db.models import Comment, User, SocialPost

# profile_edit_forms
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'photo', 
            'username', 
            'birthday', 
            'email', 
            'phone', 
            'short_bio'
        ]

class CommentSerializer(serializers.ModelSerializer):
    #https://stackoverflow.com/questions/20633313/django-rest-framework-get-related-model-field-in-serializer
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ['date_created', 'author', 'comment_text']


class SocialPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = SocialPost
        fields = [
            'id',
            'date_created', 
            'author', 
            'post_title',
            'post_photo',
            'post_text'
        ]