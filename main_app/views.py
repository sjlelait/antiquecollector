from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Antique, Admirer
from .forms import CleaningForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):  
        return render(request, 'home.html')

def about(request):  
        return render(request, 'about.html')

@login_required
def antiques_index(request):
    antiques = Antique.objects.filter(user=request.user)
    return render(request, 'antiques/index.html', {'antiques': antiques})

@login_required
def antiques_detail(request, antique_id):
    antique = Antique.objects.get(id=antique_id)
    admirers_antique_doesnt_have = Admirer.objects.exclude(id__in = antique.admirers.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'antiques/detail.html', {
        'antique': antique,
        'cleaning_form': cleaning_form,
        'admirers': admirers_antique_doesnt_have
        })

@login_required
def add_cleaning(request, antique_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.antique_id = antique_id
        new_cleaning.save()
    return redirect('antiques_detail', antique_id=antique_id)


@login_required
def assoc_admirer(request, antique_id, admirer_id):
    antique = Antique.objects.get(id=antique_id)
    antique.admirers.add(admirer_id) 
    return redirect('antiques_detail', antique_id=antique_id)

@login_required
def unassoc_admirer(request, antique_id, admirer_id):
    antique = Antique.objects.get(id=antique_id)
    antique.admirers.remove(admirer_id)
    return redirect('antiques_detail', antique_id=antique_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cats_index')
        else:
            print(form.errors)
            error_message = 'Invalid Signup - Try Again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error': error_message})




class AntiqueCreate(LoginRequiredMixin, CreateView):
    model = Antique
    fields = ('name', 'material', 'description' )
    template_name = 'antiques/antique_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AntiqueUpdate(LoginRequiredMixin, UpdateView):
    model = Antique
    fields = ('name', 'material', 'description')
    template_name = 'antiques/antique_form.html'

class AntiqueDelete(LoginRequiredMixin, DeleteView):
    model = Antique
    success_url = '/antiques/'
    template_name = 'antiques/antique_confirm_delete.html'




class AdmirerList(LoginRequiredMixin, ListView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_list.html'

class AdmirerDetail(LoginRequiredMixin, DetailView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_detail.html'

class AdmirerCreate(LoginRequiredMixin, CreateView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_form.html'

class AdmirerUpdate(LoginRequiredMixin, UpdateView):
    model = Admirer
    fields = '__all__'
    template_name = 'admirers/admirer_form.html'

class AdmirerDelete(LoginRequiredMixin, DeleteView):
    model = Admirer
    success_url = '/admirers/'
    template_name = 'admirers/admirer_confirm_delete.html'