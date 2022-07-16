from django.db import models

# Create your models here.  
class user_info(models.Model):
    user_id = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

class question_book(models.Model):
    uuid = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    image_folder = models.CharField(max_length=250)
    contents = models.JSONField()

class setting(models.Model):
    user_id = models.CharField(max_length=250)
    data = models.JSONField()
