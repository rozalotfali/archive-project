from archivesapp.models import ArchiveTypeFile
from rest_framework import serializers
from django.core.exceptions import ValidationError




class Archiveserializer(serializers.ModelSerializer):
  #filelist=serializers.FileField(required=False,allow_null=True)
  file=serializers.FileField(required=False,allow_null=True)
  audio=serializers.FileField(required=False,allow_null=True)
  text=serializers.FileField(required=False,allow_null=True)
  pic=serializers.FileField(required=False,allow_null=True)
  video=serializers.FileField(required=False,allow_null=True)
  #file_count=serializers.ListField()
  class Meta:
        model=ArchiveTypeFile
        fields=['id','mediatype','user','category','file','audio','text','pic','video']
        

  

  def validate(self, validated_data):
        #instance = super(Archiveserializer, self).validate(validated_data)
        #instance = self.validate(validated_data)
        file = validated_data.get('file')
        audio = validated_data.get('audio')
        text = validated_data.get('text')
        pic = validated_data.get('pic')
        video = validated_data.get('video')
        
        
        file_count = [file, audio, text, pic, video]
        #for item in file_count:
        if len([item for item in file_count if item ]) != 1:
            raise ValidationError("You are allowed to import one file each time.")
          
        #instance = super(Archiveserializer, self).validate(validated_data)
         
        #for item in file_count:
         #   if item:
          #    instance.save_file(item)
          
        return validated_data


  #def validate(self,validated_data):
   #     instance = super().validate(validated_data)
    #file=validated_data.pop('file')
    #    file=validated_data.get('file')
    #audio=validated_data.pop('audio')
     #   audio=validated_data.get('audio')
    #text=validated_data.pop('text')
      #  text=validated_data.get('text')
    #pic=validated_data.pop('pic')
       # pic=validated_data.get('pic')
    #video=validated_data.pop('video')
        #video=validated_data.get('video')
        
        #file_count =[file, audio, text, pic, video]  
        #for item in file_count:
          #if  len(file_count)==1 and item == 'file':  #
           # item.save()     
           # instance.save('file_name',filee)
          #if len(file_count)==1 and item == audio:      # 
            #item.save()
           # instance.save('audio_nam)e',audioo)
            #audio=self.save()
          #if len(file_count)==1 and item==text:  #
           # instance.save('audio_name',textt)
            #item.save()
          #if len(file_count)==1 and item==pic: #
           # instance.save('pic_name',picc)
            #item.save()
          #if len(file_count)==1 and item==video :   #  
           # instance.save('video_name',video)
            #item.save()
          #if len(file_count)!=1 :
         #   raise ValidationError("you are allowed to import onefile eachtime.")
        
        #return validated_data
  
    #for item in file_count:
     # if len(file_count) != 1:
      #  raise serializers.ValidationError("you are allowed to import onefile eachtime.")
    
  #def create(self,validated_data):
        #instance = super().create(validated_data)
        #file = validated_data.get('file')
        #audio = validated_data.get('audio')
        #text = validated_data.get('text')
        #pic = validated_data.get('pic')
        #video = validated_data.get('video')

       # if file:
        #  instance.file.save(file)
        #if audio:
         # instance.audio.save(audio)
        #if text:
         # instance.text.save(text)
        #if pic:
         # instance.pic.save(pic)
        #if video:
         # instance.video.save(video)

        #return instance
   
   
 
  
        
        #  if file_count ==file and len(file_count)==1:
   #    instance.file.save('file_name',file)
    #if file_count==audio and len(file_count)==1:
     # instance.audio.save('audio_name',audio)
   # if file_count==text and len(file_count)==1:
    #  instance.text.save('audio_name',text)
   # if file_count==pic and len(file_count)==1:
    #  instance.pic.save('pic_name',pic)
    #if file_count==video and len(file_count)==1:
     # instance.video.save('video_name',video)
    #else:
    #  raise ValidationError("you are allowed to import onefile eachtime.")
    
        
       #instance=super().create(validated_data) 
        
        #if video_file:
         #  instance.video.save(video_file)
           #instance.audio.save()
           #instance.pic.save()
          # instance.text.save()
           
        #if audio_file:
         #  instance.audio.save(audio_file)
        #if pic_file:
         #   instance.pic.save(pic_file)
        #if text_file:
        #    instance.text.save(text_file)
        
        #return instance

 

   
        
  
            
         

        
        
        
 
