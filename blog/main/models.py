from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=True)
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=20000)
    


    def __str__(self):
        return self.name, self.text