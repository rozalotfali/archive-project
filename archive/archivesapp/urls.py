#from . import views
from django.urls import path,include
#from . import api



urlpatterns = [
    path('api/',include('archivesapp.api.urls')),
    
    ]