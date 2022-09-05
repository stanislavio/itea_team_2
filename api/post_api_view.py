from .serializers import UserSerializer, SocialPostSerializer
from rest_framework import serializers, generics, status, mixins
from rest_framework.generics import GenericAPIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from db.models import SocialPost



class ListUserPostsView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = SocialPostSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        print("This session will expire in:", self.request.session.get_expiry_age())
        # print("CSRF:", self.request.session['csrftoken'])
        print("Session content:")
        for key in self.request.session.keys():
            print("Key:", key)
            print ("\t content:=>" + self.request.session[key])
            
        return SocialPost.objects.filter(author= self.request.user).order_by('-date_created')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)