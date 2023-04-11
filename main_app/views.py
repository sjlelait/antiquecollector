from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Antique, Admirer
from .forms import CleaningForm

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
    admirers_antique_doesnt_have = Admirer.objects.exclude(id__in = antique.admirers.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'antiques/detail.html', {
        'antique': antique,
        'cleaning_form': cleaning_form,
        'admirers': admirers_antique_doesnt_have
        })

def add_cleaning(request, antique_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.antique_id = antique_id
        new_cleaning.save()
    return redirect('antiques_detail', antique_id=antique_id)


def assoc_admirer(request, antique_id, admirer_id):
    antique = Antique.objects.get(id=antique_id)
    antique.admirers.add(admirer_id) 
    return redirect('antiques_detail', antique_id=antique_id)

def unassoc_admirer(request, antique_id, admirer_id):
    antique = Antique.objects.get(id=antique_id)
    antique.admirers.remove(admirer_id)
    return redirect('antiques_detail', antique_id=antique_id)



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




class AdmirerList(ListView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_list.html'

class AdmirerDetail(DetailView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_detail.html'

class AdmirerCreate(CreateView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_form.html'

class AdmirerUpdate(UpdateView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_form.html'

class AdmirerDelete(DeleteView):
    model = Admirer
    success_url = '/admirers/'
    template_name = 'admirers/admirer_confirm_delete.html'