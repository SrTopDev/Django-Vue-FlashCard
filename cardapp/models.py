from django.db import models

# Create your models here.  
class user_info(models.Model):
    user_id = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

