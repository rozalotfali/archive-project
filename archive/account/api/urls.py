# account/api/signup
from . import views
from django.urls import path,include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter



#router=routers.DefaultRouter()
#router.register('uservieset/',views.userviewset.as_view())
urlpatterns = [
    path('signup/',views.SignupCreateAPIView.as_view()),
    path('delete/<str:pk>',views.SignupRetrieveDestroyAPIView.as_view()),
    path('signuplist/',views.SignupListeAPIView.as_view()),
    
   
]