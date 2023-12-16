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
    path('shopping_meet/', shopping_meet, name='shopping_meet'),
    path('update_phone_detail/', update_phone_detail, name='update_phone_detail'),
    path('groupe/', groupe_view, name='groupe'),
    path('confirmer_creation_groupe/', confirmer_creation_groupe, name='confirmer_creation_groupe'),
    path('mesgroupes/<int:groupe_id>/', views.mesgroupes, name='mesgroupes'),
    path('afficher_historique/', afficher_historique, name='afficher_historique'),
    path('mesgroupes/', mesgroupes, name='mesgroupes'),
    path('mes_groupes/', mes_groupes, name='mes_groupes'),
    path('afficherMeet/',afficherMeet,name='afficherMeet'),
    path('planifier_reunion/',planifier_reunion,name='planifier_reunion'),
    path('get_participants/', get_participants, name='get_participants'),
    path('supprimer_Meet/<int:meeting_id>/', supprimer_Meet, name='supprimer_Meet'),
    path('Budjet/', Budjet, name='Budjet'),
    path('afficherBudjet/', afficher_budjet, name='afficherBudjet'),
    path('supprimer_budjet/<int:budget_id>/', supprimer_budjet, name='supprimerBudjet'),
    path('afficherBudjet/', afficher_budjet, name='afficher_budjet'),
    path('supprimer_groupe/<int:groupe_id>/', supprimer_groupe, name='supprimer_groupe'),


]