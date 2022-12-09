from django.db import models

# Create your models here.

class Recipients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    file = models.ImageField(upload_to='media/')
