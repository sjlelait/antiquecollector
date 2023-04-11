from django.db import models
from django.urls import reverse

# Create your models here.

class Admirer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admirer_detail', kwargs={'pk': self.id})

class Antique(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=75, default='Unknown')
    description = models.TextField(max_length=250, default='No description available.')
    admirers = models.ManyToManyField(Admirer)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('antiques_detail', kwargs={'antique_id': self.id})

class Cleaning(models.Model):
    CLEAN = (
        ('D', 'Dust'),
        ('P', 'Polish'),
        ('C', 'Cleaning'),
    )
    date = models.DateField('cleaning date')
    type = models.CharField(max_length=1, choices=CLEAN, default=CLEAN[0][0], verbose_name='cleaning type')
    antique = models.ForeignKey(Antique, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

