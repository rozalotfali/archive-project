#from . import views
from django.urls import path,include
#from . import api



urlpatterns = [
    path('api/',include('blog.api.urls')),
    
    ]