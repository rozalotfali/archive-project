from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    image= models.ImageField(upload_to="img",blank=True,null=True)
    
    
    
    def __str__(self):
        return self.name
    