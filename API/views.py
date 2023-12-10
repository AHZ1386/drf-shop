from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializers import UserProfileSerializer,CreateUserProfileSerializer
from rest_framework.response import Response
from .models import UserProfile

@api_view(['GET','POST'])
def  test(request):
    if request.method == 'GET':
        data = UserProfile.objects.all()
        serializer_data = UserProfileSerializer(data,many=True)
        
        return Response(serializer_data.data)
    if request.method == 'POST':
        request_data = request.data
        
        serializer = CreateUserProfileSerializer(data=request_data)
        
        
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors,status=401)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)