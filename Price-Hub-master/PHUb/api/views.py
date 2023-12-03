
import time
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render , redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Groupe, Personne, Phone
from .forms import AddPhoneForm, AdvancedSearchForm
from .models import HistoriqueVisite
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Souhaits
from .models import *



# Create your views here.
def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(username=username).first()
        if user:
            auth_user = authenticate(username=username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('home')
            else:
                messages.error(request, "Mot de passe incorrect")
        else:
                messages.error(request, "Nom d'utilisateur n'existe pas")

    return render( request, 'login.html',{})
#-----------------------------------------------------------
def sign_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
      # la partie email
        try:
            validate_email(email)
        except:
            error = True
            message = "Votre Email n'est pas valide !!!"
      # la partie password vérifier que les mots de passe sont identique
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
      # Exist si l'utilisateur existe déja on peut pas le recréer
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà !!"
        
      # S'inscrire 
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()
# enregestrer les user avec le mot de passe 
            user.password = password
            user.set_password(user.password)
            user.save()
            return redirect('log_in')
    context = {
        'error':error,
        'message':message
    }

    return render (request,'signup.html',context)
# ne pas aller au homme avant de connecter
@login_required(login_url='log_in')
def home(request):
    return render (request,'home.html',{})
def logout(request):
    return render (request,'login.html',{})
def index(request):
    return render (request,'index.html',{})
from django.shortcuts import render
from .models import Phone

def telephones(request):
    # Récupérer le paramètre de tri depuis l'URL, par défaut trier par price_USD
    sort_option = request.GET.get('sort', 'price')

    # Déterminer le champ de tri à utiliser dans la requête
    if sort_option == 'rating':
        sort_field = 'rating'
    elif sort_option == 'review':
        sort_field = 'totalReviews'
    else:
        sort_field = 'price_USD'

    # Récupérer la liste des téléphones (filtrée par recherche) et triés
    query = request.GET.get('q', '')
    phones = Phone.objects.filter(phone_name__icontains=query).order_by(sort_field)

    # Initialiser le formulaire de recherche avancée
    advanced_search_form = AdvancedSearchForm()

    # Vérifiez si le formulaire de recherche avancée a été soumis
    if 'advanced_search' in request.GET:
        # Mettez à jour le formulaire avec les données soumises
        advanced_search_form = AdvancedSearchForm(request.GET)

        # Vérifiez si le formulaire est valide
        if advanced_search_form.is_valid():
            # Récupérez les données du formulaire
            nom = advanced_search_form.cleaned_data.get('nom')
            prix_min = advanced_search_form.cleaned_data.get('prix_min')
            prix_max = advanced_search_form.cleaned_data.get('prix_max')
            ram_min = advanced_search_form.cleaned_data.get('ram_min')
            ram_max = advanced_search_form.cleaned_data.get('ram_max')
            operating_system = advanced_search_form.cleaned_data.get('operating_system')
            storage_min = advanced_search_form.cleaned_data.get('storage_min')
            storage_max = advanced_search_form.cleaned_data.get('storage_max')
            brand = advanced_search_form.cleaned_data.get('brand')  # Ajout du champ de marque

            # Construisez le filtre en fonction des champs renseignés
            filter_params = {}

            # Ajoutez les champs au filtre uniquement s'ils sont renseignés
            if nom:
                filter_params['phone_name__icontains'] = nom
            if prix_min is not None and prix_max is not None:
                filter_params['price_USD__range'] = (prix_min, prix_max)
            if ram_min is not None and ram_max is not None:
                filter_params['ram_GB__range'] = (ram_min, ram_max)
            if operating_system:
                filter_params['os__icontains'] = operating_system
            if storage_min is not None and storage_max is not None:
                filter_params['storage_GB__range'] = (storage_min, storage_max)
            if brand:
                filter_params['brand__icontains'] = brand  # Filtrer par marque

            # Filtrer les téléphones en fonction des critères de recherche avancée
            phones = phones.filter(**filter_params)

    # Gérer le formulaire d'ajout de téléphone
    if request.method == 'POST' and 'ajouter_telephone' in request.POST:
        form = AddPhoneForm(request.POST)
        if form.is_valid():
            phone_instance = form.save(commit=False)

            # Générez un identifiant unique, par exemple, en utilisant la date et l'heure actuelles
            phone_instance.identifiant = str(int(time.time()))

            phone_instance.save()  # Enregistrez le téléphone dans la base de données
            return redirect('telephones')  # Redirigez vers la page des téléphones après l'ajout
    else:
        form = AddPhoneForm()

    # Créer le contexte
    context = {
        'phones': phones,
        'query': query,
        'sort_option': sort_option,
        'advanced_search_form': advanced_search_form,
        'add_phone_form': form,  # Ajoutez le formulaire d'ajout au contexte
    }

    # Rendre le modèle avec le contexte
    return render(request, 'telephones.html', context)

def phone_detail(request, phone_id):
    phone = get_object_or_404(Phone, identifiant=phone_id)
    context = {'phone': phone}
    return render(request, 'phone_detail.html', context)

def update_phone_detail(request):
    if request.method == 'POST':
        phone_id = request.POST.get('phone_id')
        new_price = request.POST.get('new_price')

        # Validez et mettez à jour le prix dans la base de données
        phone = get_object_or_404(Phone, identifiant=phone_id)
        if new_price:
            print(f"Ancien prix : {phone.price_USD}")
            print(f"Nouveau prix : {new_price}")
            phone.new_price = new_price
            phone.price_USD = new_price  # Remplacer également le prix original
            phone.save()

    return redirect('telephones')
def tableaubord(request):
    if request.method == 'POST':
        # Récupérer l'utilisateur connecté
        user = request.user

        # Récupérer les données du formulaire
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        name = request.POST.get('name')
        store_name = request.POST.get('Nom du magasin')
        location = request.POST.get('Lieu')
        prix = request.POST.get('prix')
        date_of_visit = request.POST.get('date_of_visit')

        # Récupérer les valeurs des champs "other" si la sélection est "Autre"
        other_brand = request.POST.get('other_brand') if brand == 'other' else None
        other_name = request.POST.get('other_name') if name == 'other' else None
        other_category = request.POST.get('other_category') if category == 'other' else None

        # Validation des champs non nuls
        if brand is not None and name is not None:
            # Enregistrement dans la base de données avec l'utilisateur actuel
            historique_visite = HistoriqueVisite.objects.create(
                user=user,
                category=other_category if other_category else category,
                brand=other_brand if other_brand else brand,
                name=other_name if other_name else name,
                store_name=store_name,
                location=location,
                prix=prix,
                date_of_visit=date_of_visit,
            )

    # Récupérer toutes les visites enregistrées pour l'utilisateur actuel
    historique_visites = HistoriqueVisite.objects.filter(user=request.user)

    # Renvoyer la liste des visites dans le contexte de la page tableau de bord
    return render(request, 'tableaubord.html', {'historique_visites': historique_visites})
def histoire(request):
    name = Phone.objects.values_list('phone_name', flat=True).distinct()
    brand = Phone.objects.values_list('brand', flat=True).distinct()
    return render(request, 'histoire.html', {'name': name, 'brand': brand})
def supprimer_visite(request, visite_id):
    # Filtrer la visite basée sur l'utilisateur actuel
    visite = get_object_or_404(HistoriqueVisite, pk=visite_id, user=request.user)
    visite.delete()
    return redirect('tableaubord')

def souhaits(request):
    name = Phone.objects.values_list('phone_name', flat=True).distinct()
    brand = Phone.objects.values_list('brand', flat=True).distinct()

    # Filtrer les souhaits basés sur l'utilisateur actuel
    souhaits = Souhaits.objects.filter(user=request.user)

    return render(request, 'souhaits.html', {'name': name, 'brand': brand, 'souhaits': souhaits})

def save_souhaits(request):
    if request.method == 'POST':
        user = request.user
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        # Récupérer les valeurs des champs "other" si la sélection est "Autre"
        other_brand = request.POST.get('other_brand') if brand == 'other' else None
        other_name = request.POST.get('other_name') if name == 'other' else None
        other_category = request.POST.get('other_category') if category == 'other' else None
        if brand is not None and name is not None:
           Souhaits.objects.create(
            category=other_category if other_category else category,
            brand=other_brand if other_brand else brand,
            name=other_name if other_name else name,
            user=user,
            phone_number=phone_number)
        return JsonResponse({'message': 'Les souhaits ont été enregistrés avec succès!'})
    else:
        return JsonResponse({'message': 'La requête n\'est pas de type POST'})
def afficherSouhaits(request):
    # Filtrer les souhaits basés sur l'utilisateur actuel
    MesSouhaits = Souhaits.objects.filter(user=request.user)
    return render(request, 'afficherSouhaits.html', {'MesSouhaits': MesSouhaits})
def supprimer_souhaits(request, souhaits_id):
    # Filtrer les souhaits basés sur l'utilisateur actuel
    souhaits = get_object_or_404(Souhaits, pk=souhaits_id, user=request.user)
    souhaits.delete()
    return redirect('afficherSouhaits')
def changer_statut(request, souhait_id):
    if request.method == 'POST':
        # Filtrer le souhait basé sur l'utilisateur actuel
        souhait = get_object_or_404(Souhaits, pk=souhait_id, user=request.user)
        # Mettez à jour le statut comme vous le souhaitez
        souhait.status = 'Clôturé'
        souhait.save()
        return JsonResponse({'success': True, 'nouveau_statut': souhait.status}) 
    else:
        return JsonResponse({'success': False})
        
def groupe_view(request):
    categories = Souhaits.objects.values_list('category', flat=True).distinct()
    marques = Souhaits.objects.values_list('brand', flat=True).distinct()
    noms = Souhaits.objects.values_list('name', flat=True).distinct()

    if request.method == 'POST':
        # Traitement du formulaire de création de groupe
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        name = request.POST.get('name')

        # Autres logiques de traitement du formulaire, si nécessaire

        # Récupération des personnes ayant le même souhait
        personnes_du_groupe = Souhaits.objects.filter(category=category, brand=brand, name=name)

        return render(request, 'groupe.html', {'categories': categories, 'marques': marques, 'noms': noms, 'personnes_du_groupe': personnes_du_groupe, 'category': category, 'brand': brand, 'name': name})
    else:
        return render(request, 'groupe.html', {'categories': categories, 'marques': marques, 'noms': noms})

def confirmer_creation_groupe(request):
    if request.method == 'POST':
        personnes_selectionnees_ids = request.POST.getlist('personnes_selectionnees')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        name = request.POST.get('name')
        user = request.user  # Récupérer l'utilisateur actuel

        # Vérifier si un groupe avec les mêmes caractéristiques existe déjà
        existing_group = Groupe.objects.filter(
            category=category,
            brand=brand,
            name=name,
        ).first()

        if existing_group:
            # Ajouter les personnes sélectionnées au groupe existant
            personnes_du_groupe = Souhaits.objects.filter(id__in=personnes_selectionnees_ids)
            existing_group.personnes.add(*personnes_du_groupe)

            return render(request, 'mesgroupes.html', {'groupe': existing_group, 'category': category, 'brand': brand, 'name': name, 'personnes_du_groupe': personnes_du_groupe})
        else:

            return JsonResponse({'success': False})
def shopping_meet(request):

    return render(request, 'ShoppingMeet.html', {})
            # Créer un nouveau groupe
    groupe = Groupe.objects.create(
                user=user,
                nom=f"Groupe {category}",
                souhait_commun=f"{category} - {brand} - {name}",
                category=category, 
                brand=brand,
                name=name
            )

            # Ajouter les personnes sélectionnées au nouveau groupe
    personnes_du_groupe = Souhaits.objects.filter(id__in=personnes_selectionnees_ids)
    groupe.personnes.add(*personnes_du_groupe)

    return render(request, 'mesgroupes.html', {'groupe': groupe, 'category': category, 'brand': brand, 'name': name, 'personnes_du_groupe': personnes_du_groupe})

    return redirect('mes_groupes')
def mesgroupes(request, groupe_id):
    groupe = get_object_or_404(Groupe, id=groupe_id)
    groupes_uniques = set(Groupe.objects.all())  # Utilisation d'un ensemble pour des groupes uniques

    personnes_du_groupe = groupe.personnes.all()

    return render(request, 'mesgroupes.html', {'groupes': groupes_uniques, 'groupe': groupe, 'personnes_du_groupe': personnes_du_groupe})

def afficher_historique(request):
    if request.method == 'POST':
        personne_id = request.POST.get('personne_id')
        
        try:
            # Utilisez get_object_or_404 pour vous assurer que l'utilisateur existe
            personne = get_object_or_404(Souhaits, id=personne_id)
        except Souhaits.DoesNotExist:
            # Gérer l'erreur ici
            return HttpResponseBadRequest("Personne non trouvée")

        # Filtrer l'historique par le nom de produit et le souhait commun ET l'utilisateur
        historique = HistoriqueVisite.objects.filter(
            name=personne.name,
            category=personne.category,
            brand=personne.brand,
            user=personne.user  # Ajoutez cette condition pour filtrer par utilisateur
        )
        
        return render(request, 'afficherhisto.html', {'historique': historique, 'personne': personne})

    # Gérer le cas où la requête n'est pas POST
    return HttpResponseBadRequest("Méthode non autorisée")
def mes_groupes(request):
    # Récupérer l'ID de l'utilisateur connecté
    user_id = request.user.id

    if request.user.is_authenticated:
        # Filtrer les groupes par l'ID de l'utilisateur connecté
        groupes = Groupe.objects.filter(user_id=user_id)
        return render(request, 'mes_groupes.html', {'groupes': groupes})
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        return redirect('nom_de_votre_page_de_connexion')
    MesSouhaits = Souhaits.objects.all()
    return render(request, 'ShoppingMeet.html', {'MesSouhaits': MesSouhaits})


def planifier_reunion(request):
    if request.method == 'POST':
        category_meet = request.POST.get('category')
        souhaits_participants = Souhaits.objects.filter(category=category_meet)

        meeting = Meeting.objects.create(
            user=request.user,
            category=category_meet,
            store_name=request.POST.get('Nom du magasin'),
            location=request.POST.get('Lieu'),
            date_of_meeting=request.POST.get('date_of_visit')
        )

        meeting.participants.set(souhaits_participants)

        return JsonResponse({'message': 'Le meeting a été enregistré avec succès!'})
    else:
        return JsonResponse({'message': 'La requête n\'est pas de type POST'})


def afficherMeet(request):
    user_meetings = Meeting.objects.filter(user=request.user)
    return render(request, 'afficherMeet.html', {'Meet': user_meetings})
def get_participants(request):
    category_id = request.GET.get('category')
    participants = Souhaits.objects.filter(category=category_id).values('user__id', 'user__username').distinct()
    return JsonResponse(list(participants), safe=False)

def supprimer_Meet(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting.delete()
    return redirect('afficherMeet')

 