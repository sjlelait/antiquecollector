from django.contrib import admin

# Register your models here.
from .models import Antique, Cleaning, Admirer

admin.site.register([Antique, Cleaning, Admirer])