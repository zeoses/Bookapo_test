from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework import viewsets, status, views
from .models import Profile 
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions
from datetime import datetime

class ProfileViewSet(viewsets.ViewSet):
    """

    get : get user details and update user activity time

    """
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        """ get loggin user details"""
        if type(self.request.user) is User:
            if self.request.user.profile:
                self.request.user.profile.last_activity_time = datetime.now()
                self.request.user.profile.save()
                
                profile = Profile.objects.filter(pk=self.request.user.profile.pk)
                serializer = ProfileSerializer(profile, many=True)
                return Response(serializer.data)
                
                
        return Response({'message': {
                    'title': "Not Found",
                    'description': 'not match profile with user account',
                }
            }, status=status.HTTP_404_NOT_FOUND)
