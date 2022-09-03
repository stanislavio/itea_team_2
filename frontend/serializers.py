from rest_framework import serializers
from db.models import Comment, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',  'last_login', 'short_bio', 'photo', 'birthday', 'phone']



class CommentSerializer(serializers.ModelSerializer):
    #https://stackoverflow.com/questions/20633313/django-rest-framework-get-related-model-field-in-serializer
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ['date_created', 'author', 'comment_text']



