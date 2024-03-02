#from . import views
from django.urls import path,include
#from . import api



urlpatterns = [
    path('api/',include('account.api.urls')),
    #path('viewgeni/',views.userviewset.as_view()),
    #path('viewgeni/<str:pk>',views.usergenericviewset.as_view()),
    ]
