from django.db import models

# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=255)
    latency = models.CharField(max_length=255)
    type = models.IntegerField(default=0)
    platform = models.CharField(max_length=255)
    hour = models.DateTimeField(auto_now_add=True, blank=True)