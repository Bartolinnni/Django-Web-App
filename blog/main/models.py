from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=20000)
    
    def __str__(self):
        return self.name, self.text