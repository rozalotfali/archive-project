# account/api/signup
from . import views
from django.urls import path,include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('createarchivepost/',views.ArchivesCreateAPIView.as_view()),
    path('archivepostlist/',views.ArchivesListAPIView.as_view()),
    path('archivesitemdelete/<int:pk>',views.ArchivesDestoryAPIView.as_view())
   
]