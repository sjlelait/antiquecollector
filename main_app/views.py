from django.shortcuts import render
from .models import Antique

# Create your views here.
def home(request):  
        return render(request, 'home.html')

def about(request):  
        return render(request, 'about.html')

def antiques_index(request):
    antiques = Antique.objects.all()
    return render(request, 'antiques/index.html', {'antiques': antiques})

def antiques_detail(request, antique_id):
    antique = Antique.objects.get(id=antique_id)
    return render(request, 'antiques/detail.html', {'antique': antique})