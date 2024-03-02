from django.shortcuts import render
from account.models import CustomUser
from .serializers import Userserializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


user=get_user_model()
#class userviewset(viewsets.ModelViewSet):
    #queryset=CustomUser.objects.all()
    #serializer_class=Userserializer
    
#baraye user mitonim createconim ya delete ya update  
class SignupListeAPIView(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=Userserializer
class SignupCreateAPIView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=Userserializer
    
class SignupRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=Userserializer
    

    
    
# function based:
# def name_continue
# class based:
# class NameContinue
    
    



