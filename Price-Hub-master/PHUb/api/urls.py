
from django import views
from django.urls import  path
from .views import *
from . import views

urlpatterns = [
    path('',index,name='index'),
    path('log_in/',log_in,name='log_in'),
    path('signup/',sign_up,name='sign_up'),
    path('logout/',logout,name='logout'),
    path('home/',home,name='home'),
    path('telephones/',telephones,name='telephones'),
    path('telephones/<str:phone_id>/', phone_detail, name='phone_detail'),
    path('histoire/',histoire,name='histoire'),
    path('tableaubord/',tableaubord,name='tableaubord'),
    path('afficherSouhaits/',afficherSouhaits,name='afficherSouhaits'),
    path('souhaits/',souhaits,name='souhaits'),
    path('save_souhaits/', save_souhaits, name='save_souhaits'),
    path('supprimer_visite/<int:visite_id>/', views.supprimer_visite, name='supprimer_visite'),
    path('supprimer_souhaits/<int:souhaits_id>/', views.supprimer_souhaits, name='supprimer_souhaits'),
    path('changer_statut/<int:souhait_id>/', changer_statut, name='changer_statut'),
    path('update_phone_detail/', update_phone_detail, name='update_phone_detail'),
]