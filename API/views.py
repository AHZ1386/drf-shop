from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializers import UserProfileSerializer,CreateUserProfileSerializer
from rest_framework.response import Response
from .models import UserProfile
from rest_framework.status import HTTP_204_NO_CONTENT

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
    

@api_view(["PUT","DELETE"])
def  update_test(request,id):
    
    if request.mothed =='PUT':
        user_profile = UserProfile.objects.get(id=id)
        serializer = UserProfileSerializer(
        instance = user_profile,
        data = request.data
        )
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data,status=200)
@api_view(["DELETE"])
def delete_test(reqeust,id):
    user_profile = UserProfile.objects.get(id=id)
    user_profile.delete()
    return Response(status=HTTP_204_NO_CONTENT)