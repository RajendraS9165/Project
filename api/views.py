from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume Upload Successfully !!! ', 'status':'Success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self, request, format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({'status':'Success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        
        
        