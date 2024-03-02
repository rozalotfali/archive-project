# account/api/signup
from . import views
from django.urls import path,include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('postcreted/',views.BlogPostCreateAPIView.as_view()),
    path('posts/',views.BlogPostListAPIView.as_view()),
    path('BlogPostUpdateDelete/<int:pk>',views.BlogPostUpdateDeleteAPIView.as_view())
   
]