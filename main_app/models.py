from django.db import models

# Create your models here.

class Antique(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=75, default='Unknown')
    description = models.TextField(max_length=250, default='No description available.')

    def __str__(self):
        return self.name