from rest_framework import serializers
from db.models import User


# profile_edit_forms
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['photo', 'username', 'birthday', 'email', 'phone', 'short_bio']
