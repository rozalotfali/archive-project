from django.shortcuts import render
from category.models import Category
from .serializer import CategorySerializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination


#blogpost
class CategoryCreateAPIView(generics.CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
class CategoryListAPIView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class=LimitOffsetPagination
class CategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class=LimitOffsetPagination
