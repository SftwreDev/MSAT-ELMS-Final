from django.db import models


class Handouts(models.Model):
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length = 200)
    documents = models.FileField(upload_to='handouts')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Videos(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length = 200)
    description = models.CharField(max_length=300)
    video = models.FileField(upload_to="videos")
    uploaded_at = models.DateTimeField(auto_now_add=True)
