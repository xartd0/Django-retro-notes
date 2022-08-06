from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=500)
    uniq = models.CharField(max_length=30, unique=True)