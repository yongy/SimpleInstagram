from django.shortcuts import render
from rest_framework import generics
from Insta.models import Post
from .serializers import PostSerializer
# Create your views here.

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer