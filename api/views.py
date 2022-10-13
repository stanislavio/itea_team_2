from rest_framework.response import Response
from rest_framework import status
from db.models import User
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.views import APIView
# from rest_framework.authentication import TokenAuthentication


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

    def get(self, request):
        query = User.objects.all()
        serializer = UserSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
