from rest_framework import serializers
from db.models import User

from db.models import Comment, User, SocialPost, TrainingPost

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
    author = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = [
            'id',
            'date_created', 
            'author', 
            'comment_text'
        ]


class SocialPostSerializer(serializers.ModelSerializer):
    post_type = serializers.SerializerMethodField('post_type_func')

    author = UserSerializer()

    def post_type_func(self, obj):
        return "social"

    class Meta:
        model = SocialPost
        fields = [
            'id',
            'date_created', 
            'author', 
            'post_title',
            'post_photo',
            'post_text',
            'post_type',
        ]


class TrainingPostSerializer(serializers.ModelSerializer):
    post_type = serializers.SerializerMethodField('post_type_func')

    author = UserSerializer()

    def post_type_func(self, obj):
        return "training"

    class Meta:
        model = TrainingPost
        fields = [
            'id',
            'date_created', 
            'author', 
            'post_title',
            'post_photo',
            'post_text',
            'post_type',
        ]