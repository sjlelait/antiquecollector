from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('antiques/', views.antiques_index, name='antiques_index'),
    path('antiques/<int:antique_id>/', views.antiques_detail, name='antiques_detail'),
]