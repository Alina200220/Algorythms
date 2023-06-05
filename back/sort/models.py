from django.db import models

class Sort(models.Model):
    array=models.CharField(max_length=250)
    n=models.IntegerField()
