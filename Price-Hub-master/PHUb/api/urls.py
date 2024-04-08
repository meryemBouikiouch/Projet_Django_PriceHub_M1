from django import views
from django.urls import  path
from .views import *
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet


urlpatterns = [
    path('',index,name='index'),
    path('log_in/',log_in,name='log_in'),
    path('signup/',sign_up,name='sign_up'),
    path('logout/',logout,name='logout'),
    path('home/',home,name='home'),
    path('telephones/',telephones,name='telephones'),
    path('ordinateur/', ordinateur, name='ordinateur'),

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

    path('communaute/',communaute,name='communaute'),
    path('communaute_telephone/',communaute_telephone,name='communaute_telephone'),
    path('sujets_telephone/creer_telephone/', views.creer_sujet_telephone, name='creer_sujet_telephone'),
    path('sujets_telephone/<int:sujet_telephone_id>/', views.details_sujet_telephone, name='details_sujet_telephone'),
    path('sujets_telephone/supprimer_telephone/<int:sujet_telephone_id>/', views.supprimer_sujet_telephone, name='supprimer_sujet_telephone'),


    path('communaute_tablette/',communaute_tablette,name='communaute_tablette'),
    path('sujets_tablette/creer_tablette/', views.creer_sujet_tablette, name='creer_sujet_tablette'),
    path('sujets_tablette/<int:sujet_tablette_id>/', views.details_sujet_tablette, name='details_sujet_tablette'),
    path('sujets_tablette/supprimer_tablette/<int:sujet_tablette_id>/', views.supprimer_sujet_tablette, name='supprimer_sujet_tablette'),



    path('communaute_ordinateur/',communaute_ordinateur,name='communaute_ordinateur'),
    path('sujets_ordinateur/creer_ordinateur/', views.creer_sujet_ordinateur, name='creer_sujet_ordinateur'),
    path('sujets_ordinateur/<int:sujet_ordinateur_id>/', views.details_sujet_ordinateur, name='details_sujet_ordinateur'),
    path('sujets_ordinateur/supprimer_ordinateur/<int:sujet_ordinateur_id>/', views.supprimer_sujet_ordinateur, name='supprimer_sujet_ordinateur'),


    path('communaute_Accessoire_telephone/',communaute_Accessoire_telephone,name='communaute_Accessoire_telephone'),
    path('sujets_Accessoire_telephone/creer_Accessoire_telephone/', views.creer_sujet_Accessoire_telephone, name='creer_sujet_Accessoire_telephone'),
    path('sujets_Accessoire_telephone/<int:sujet_Accessoire_telephone_id>/', views.details_sujet_Accessoire_telephone, name='details_sujet_Accessoire_telephone'),
    path('sujets_Accessoire_telephone/supprimer_Accessoire_telephone/<int:sujet_Accessoire_telephone_id>/', views.supprimer_sujet_Accessoire_telephone, name='supprimer_sujet_Accessoire_telephone'),


    path('communaute_Accessoire_ordinateur/',communaute_Accessoire_ordinateur,name='communaute_Accessoire_ordinateur'),
    path('sujets_Accessoire_ordinateur/creer_Accessoire_ordinateur/', views.creer_sujet_Accessoire_ordinateur, name='creer_sujet_Accessoire_ordinateur'),
    path('sujets_Accessoire_ordinateur/<int:sujet_Accessoire_ordinateur_id>/', views.details_sujet_Accessoire_ordinateur, name='details_sujet_Accessoire_ordinateur'),
    path('sujets_Accessoire_ordinateur/supprimer_Accessoire_ordinateur/<int:sujet_Accessoire_ordinateur_id>/', views.supprimer_sujet_Accessoire_ordinateur, name='supprimer_sujet_Accessoire_ordinateur'),


    path('communaute_Accessoire_tablette/',communaute_Accessoire_tablette,name='communaute_Accessoire_tablette'),
    path('sujets_Accessoire_tablette/creer_Accessoire_tablette/', views.creer_sujet_Accessoire_tablette, name='creer_sujet_Accessoire_tablette'),
    path('sujets_Accessoire_tablette/<int:sujet_Accessoire_tablette_id>/', views.details_sujet_Accessoire_tablette, name='details_sujet_Accessoire_tablette'),
    path('sujets_Accessoire_tablette/supprimer_Accessoire_tablette/<int:sujet_Accessoire_tablette_id>/', views.supprimer_sujet_Accessoire_tablette, name='supprimer_sujet_Accessoire_tablette'),



    path('Budjet/', Budjet, name='Budjet'),
    path('afficherBudjet/', afficher_budjet, name='afficherBudjet'),
    path('supprimer_budjet/<int:budget_id>/', supprimer_budjet, name='supprimerBudjet'),
    path('afficherBudjet/', afficher_budjet, name='afficher_budjet'),
    path('supprimer_groupe/<int:groupe_id>/', supprimer_groupe, name='supprimer_groupe'),

    path('carte/', carte, name='carte'),


    path('inviter-ami/', views.inviter_ami, name='inviter_ami'),
    path('confirmation-invitation/', views.confirmation_invitation, name='confirmation_invitation'),
    path('ajouter_favori/<str:phone_id>/', views.ajouter_favori, name='ajouter_favori'),
    path('retirer_favori/<str:phone_id>/', views.retirer_favori, name='retirer_favori'),
    path('mes_favoris/', views.mes_favoris, name='mes_favoris'),





]
