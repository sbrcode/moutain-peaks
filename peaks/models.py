from django.db import models

# Create your models here.
class PeakLocation(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    altitude = models.IntegerField(default=0)
    def __str__(self):
        return self.name
