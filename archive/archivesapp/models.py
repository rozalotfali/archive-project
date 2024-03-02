from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.core.exceptions import ValidationError
from category.models import Category
#from audiofield.fields import AudioField
import os.path
from  django.contrib.auth import get_user_model

user=get_user_model()



class ArchiveTypeFile(models.Model):
    type_is_file = 'F'
    type_is_Audio = 'A'
    type_is_Text = 'T'
    type_is_Pic = 'P'
    type_is_video = 'V'

    filetype_choices = [
     (type_is_file, 'File'),
     (type_is_Audio, 'Audio'),
     (type_is_Text, 'Text'),
     (type_is_Pic, 'Picture'),
     (type_is_video, 'Video'),
   ]
    mediatype=models.CharField(max_length=1,choices=filetype_choices,blank=True,null=True)
    #fileupload=models.ForeignKey(ArchivesModel,on_delete=models.CASCADE,blank=True,null=True)
    file=models.FileField(upload_to='files/', validators=[FileExtensionValidator(allowed_extensions=['pdf','html','xml','csv'])],blank=True,null=True)
    audio=models.FileField(upload_to='audio_files/', validators=[FileExtensionValidator(allowed_extensions=['mp3','WAV','VMA'])],blank=True,null=True)
    text=models.FileField(upload_to='audio_files/', validators=[FileExtensionValidator(allowed_extensions=['txt'])],blank=True,null=True)
    pic=models.ImageField(upload_to="img",blank=True,null=True)
    video=models.FileField(upload_to='vidio/', validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv'])],blank=True,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    #
    
    def save_file(self, file):
        if self.file and file.field_name == 'file':
            self.file.save(file.name, file)
        elif self.audio and file.field_name == 'audio':
            self.audio.save(file.name, file)
        elif self.text and file.field_name == 'text':
            self.text.save(file.name, file)
        elif self.pic and file.field_name == 'pic':
            self.pic.save(file.name, file)
        elif self.video and file.field_name == 'video':
            self.video.save(file.name, file)
        else:
            raise ValidationError("invalid")
    
    #class ArchivesModel(models.Model):
     #  choosefile=ArchiveTypeFile[file,audio,text,pic,video]
    #def create(self):
     #   media=validated_data[file,audio,text,pic,video]
   
            

  

   
   

    

