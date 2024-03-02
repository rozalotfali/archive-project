# account/api/signup
from . import views
from django.urls import path,include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('category/',views.CategoryListAPIView.as_view()),
    path('categorycreate/',views.CategoryCreateAPIView.as_view()),
    path('CategoryUpdateDelete/<int:pk>',views.CategoryUpdateDeleteAPIView.as_view())
   
]