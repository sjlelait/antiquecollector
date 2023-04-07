from django.db import models
from django.urls import reverse

# Create your models here.

class Antique(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=75, default='Unknown')
    description = models.TextField(max_length=250, default='No description available.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('antiques_detail', kwargs={'antique_id': self.id})