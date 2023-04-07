from django.shortcuts import render
from .models import Antique
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class AntiqueCreate(CreateView):
    model = Antique
    fields = '__all__'
    template_name = 'antiques/antique_form.html'

class AntiqueUpdate(UpdateView):
    model = Antique
    fields = ('name', 'description')
    template_name = 'antiques/antique_form.html'

class AntiqueDelete(DeleteView):
    model = Antique
    success_url = '/antiques/'
    template_name = 'antiques/antique_confirm_delete.html'