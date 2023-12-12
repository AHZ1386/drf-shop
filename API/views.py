from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializers import UserProfileSerializer,CreateUserProfileSerializer
from .models import UserProfile
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.response import Response

class UserProfileView(APIView):
    def post(request,id):
        serializer = CreateUserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    def get(self,request):
        all_user = UserProfile.objects.all()
        serializer = UserProfileSerializer(data=all_user,many=True)
        serializer.is_valid()
        print(serializer.data)
        return Response(serializer.data)
    
    def put(request,id):
        user_profile = UserProfile.objects.get(id=id) 
        serializer = UserProfileSerializer(instance=user_profile,data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    def delete(request):
        user_profile = UserProfile.objects.get(id=id)
        user_profile.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        
