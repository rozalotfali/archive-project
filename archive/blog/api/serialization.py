from blog.models import Blog
from rest_framework import serializers


class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','title','content','author','pic','created']
        
