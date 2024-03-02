from django.shortcuts import render
from archivesapp.models import ArchiveTypeFile
from .serializer import Archiveserializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django.core.exceptions import ValidationError


#archivessppcreate
class ArchivesListAPIView(generics.ListAPIView):
    queryset=ArchiveTypeFile.objects.all()
    serializer_class=Archiveserializer
    pagination_class=LimitOffsetPagination
class ArchivesCreateAPIView(generics.CreateAPIView):
    queryset=ArchiveTypeFile.objects.all()
    serializer_class=Archiveserializer
class ArchivesDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ArchiveTypeFile.objects.all()
    serializer_class=Archiveserializer
    
    

    #def get_queryset(self):
        #return ArchiveTypeFile.objects.filter()
#class ArchivesItemListAPIView(generics.ListAPIView):
   # queryset=ArchivesModel.objects.all()
    #serializer_class=ArchiveItemserializer
#class ArchivesItemCreateAPIView(generics.CreateAPIView):
 #  queryset=ArchivesModel.objects.all()
  # serializer_class=ArchiveItemserializer
  
  
 # def get(self,request:Request):
 # post=ArchiveTypeFile.objects.all()
 # postserializer=Archiveserializer(post)
 # return Response(postserializer.data)
 # def post(self,request:Request):
 # postserializer=Archiveserializer(data=request)
 # if postserializer.is_valid():
 # postserializer.save()
 # if request.FILES.getlist('file'):
 # files=request.FILES.getlist('file')
 # return files
 # return Response(postserializer.data)
 
 #clasbasedview   
#class ArchivesappCreateAPIView(generics.CreateAPIView): 
 #   queryset=ArchiveTypeFile.objects.all()
  #  serializer_class=Archiveserializer
   
   # def gr(self,request:Request):
    #    if request.FILES.getlist('file'):
     #           files=request.FILES.getlist('file')
      #          return files
            
       # return Response(request.data)
            
        #return Response(postserializer.data)
            
            
        
        
            
   #   return Response(postserializer.data,status=status.HTTP_200_OK)
  #def post(self,request:Request):
     # postserializer=Archiveserializer(data=request.data)
      
      
    


   