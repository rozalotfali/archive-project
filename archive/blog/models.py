from django.db import models
from  django.contrib.auth import get_user_model

user=get_user_model()
class Blog(models.Model):
    title=models.CharField(max_length=250,null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    author=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to="img",null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    piority=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.title 
    