from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializers import UserProfileSerializer
from rest_framework.response import Response
from .models import UserProfile

@api_view(['GET'])
def  test(request):
    data = UserProfile.objects.all()
    serializer_data = UserProfileSerializer(data,many=True)
    
    return Response(serializer_data.data)