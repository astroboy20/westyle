from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime, date
# from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =models.TextField()
    # body =RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    header_image = models.ImageField(null=True, blank =True, upload_to="Images/")
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("Blog")  #, args =(str(self.id)))
    
    