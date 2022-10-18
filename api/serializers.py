from rest_framework import serializers

from db.models import Comment, User, SocialPost, TrainingPost, RunTrainingPost, HikeTrainingPost, SwimTrainingPost



# profile_edit_forms

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match. '})
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 
            'photo', 
            'username',
            'email', 
            'phone', 
            'short_bio',
            'get_friends_number',
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
        # return str(type(obj))
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

class RunTrainingPostSerializer(TrainingPostSerializer):
    def post_type_func(self, obj):
        # return str(type(obj))
        return "running"

    class Meta:
        model = RunTrainingPost
        # fields = [
        #     'total_km_ran'
        # ]
        exclude = [
            'comments'
        ]

class HikeTrainingPostSerializer(TrainingPostSerializer):
    def post_type_func(self, obj):
        # return str(type(obj))
        return "hiking"

    class Meta:
        model = HikeTrainingPost
        # fields = [
        #     'total_km_walked'
        # ]
        # fields = "__all__"
        exclude = [
            'comments'
        ]

class SwimTrainingPostSerializer(TrainingPostSerializer):
    def post_type_func(self, obj):
        # return str(type(obj))
        return "swimming"

    class Meta:
        model = SwimTrainingPost
        # fields = [
        #     'total_km_walked'
        # ]
        # fields = "__all__"
        exclude = [
            'comments'
        ]