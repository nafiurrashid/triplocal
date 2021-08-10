from django.db import models

# Create your models here.
class Destination(models.Model):
    
     name= models.CharField(max_length=100)
     img= models.ImageField(upload_to='pics')
     desc=models.TextField()
     price= models.IntegerField()
     offer= models.BooleanField(default=False)

class testimonial(models.Model):
    
     name= models.CharField(max_length=100)
     designation= models.CharField(max_length=100)
     testimonial=models.TextField()
   

  
    