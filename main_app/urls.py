from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('antiques/', views.antiques_index, name='antiques_index'),
    path('antiques/<int:antique_id>/', views.antiques_detail, name='antiques_detail'),
    path('antiques/create/', views.AntiqueCreate.as_view(), name='antique_create'),
    path('antiques/<int:pk>/update/', views.AntiqueUpdate.as_view(), name='antique_update'),
    path('antiques/<int:pk>/delete/', views.AntiqueDelete.as_view(), name='antique_delete'),
    path('antiques/<int:antique_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('admirers/', views.AdmirerList.as_view(), name='admirer_list'),
    path('admirers/<int:pk>/', views.AdmirerDetail.as_view(), name='admirer_detail'),
    path('admirers/create/', views.AdmirerCreate.as_view(), name='admirer_create'),
    path('admirers/<int:pk>/update/', views.AdmirerUpdate.as_view(), name='admirer_update'),
    path('admirers/<int:pk>/delete/', views.AdmirerDelete.as_view(), name='admirer_delete'),
    path('antiques/<int:antique_id>/assoc_admirer/<int:admirer_id>/', views.assoc_admirer, name='assoc_admirer'),
    path('antiques/<int:antique_id>/unassoc_admirer/<int:admirer_id>/', views.unassoc_admirer, name='unassoc_admirer'),
]