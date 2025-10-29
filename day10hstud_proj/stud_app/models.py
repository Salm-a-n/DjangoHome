from django.db import models
class Std_manage(models.Model):
    name=models.CharField(max_length=50)
    standard=models.CharField(max_length=50)
    age=models.IntegerField()
