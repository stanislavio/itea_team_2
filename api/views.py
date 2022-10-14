from rest_framework.response import Response
from rest_framework import status
from db.models import User, Post
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.views import APIView
# from rest_framework.authentication import TokenAuthentication


# user_register
class RegistrationAPIView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "Registration was successful"
            data["email"] = user.email
            data["username"] = user.username
        else:
            data = serializer.errors
        return Response(data)


# user_page
class UserListAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    def get(self, request, user_id=None):

        if request.user.id == user_id or user_id is None:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        elif request.user.id != user_id:
            account = User.objects.get(pk=user_id)
            serializer = UserSerializer(account)
            return Response(serializer.data,)

    def put(self, request, user_id=None):
        if request.user.id == user_id or user_id is None:
            user = request.user
            serializer = UserSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_403_FORBIDDEN)
