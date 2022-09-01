from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from db.models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#user_page
@csrf_exempt
def user_list(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser() .parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) # HTTP response created
        return JsonResponse(serializer.errors, status=400) # HTTP response Bad Request