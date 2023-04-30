from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='')
    post = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # category = models.CharField(max_length=50,default='blog')
    

    def __str__(self):
        return self.title