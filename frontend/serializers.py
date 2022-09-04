from rest_framework import serializers
from db.models import Comment, User, SocialPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'last_login', 
            'short_bio', 
            'photo', 
            'birthday', 
            'phone'
        ]






