from django.shortcuts import render
from blog.models import Blog
from .serialization import Blogserializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


#blogpost
class BlogPostCreateAPIView(generics.CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=Blogserializer
 #clasbasedview   
class Blogpost(APIView):
  def get(self,request:Request,todoid:int):
       post=Blog.objects.get(todoid=id)
       postserializer=Blogserializer(post,many=True)
       return Response(postserializer.data,status=status.HTTP_200_OK)

class BlogPostListAPIView(generics.ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=Blogserializer
class BlogPostUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=Blogserializer

     
    
    