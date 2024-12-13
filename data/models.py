from django.db import models
from sorl.thumbnail import ImageField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption= models.CharField(max_length=500, default="")
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class ProfileData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post', null=True, blank=True)
    password2 = models.CharField(max_length=100);
    def __str__(self):
        return self.name