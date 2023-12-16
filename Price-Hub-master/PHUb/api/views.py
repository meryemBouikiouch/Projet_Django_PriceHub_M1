import time
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render , redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Phone
from .forms import AddPhoneForm, AdvancedSearchForm
from .models import HistoriqueVisite
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Souhaits
from .models import *
from .forms import *



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

def ordinateur(request):
    ordinateurs = Ordinateur.objects.all()
    return render(request, 'ordinateur.html', {'ordinateurs': ordinateurs})

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
            # Enregistrement dans la base de données
            historique_visite= HistoriqueVisite.objects.create(
                category=other_category if other_category else category,
                brand=other_brand if other_brand else brand,
                name=other_name if other_name else name,
                store_name=store_name,
                location=location,
                prix=prix,
                date_of_visit=date_of_visit,
            )

    # Récupérer toutes les visites enregistrées
    historique_visites = HistoriqueVisite.objects.all()

    # Renvoyer la liste des visites dans le contexte de la page tableau de bord
    return render(request, 'tableaubord.html', {'historique_visites': historique_visites})

def histoire(request):
    name = Phone.objects.values_list('phone_name', flat=True).distinct()
    brand = Phone.objects.values_list('brand', flat=True).distinct()
    return render(request, 'histoire.html', {'name': name, 'brand': brand})
def supprimer_visite(request, visite_id):
    visite = get_object_or_404(HistoriqueVisite, pk=visite_id)
    visite.delete()
    return redirect('tableaubord')

def souhaits(request):
    name = Phone.objects.values_list('phone_name', flat=True).distinct()
    brand = Phone.objects.values_list('brand', flat=True).distinct()
    return render (request,'souhaits.html',{'name': name, 'brand': brand})
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
    MesSouhaits = Souhaits.objects.all()
    return render(request, 'afficherSouhaits.html', {'MesSouhaits': MesSouhaits})
def supprimer_souhaits(request, souhaits_id):
    souhaits = get_object_or_404(Souhaits, pk=souhaits_id)
    souhaits.delete()
    return redirect('afficherSouhaits')
def changer_statut(request, souhait_id):
        if request.method == 'POST':
            souhait = Souhaits.objects.get(pk=souhait_id)
            # Mettez à jour le statut comme vous le souhaitez
            souhait.status = 'Clôturé'
            souhait.save()
            return JsonResponse({'success': True, 'nouveau_statut': souhait.status}) 
        else:
            return JsonResponse({'success': False})
    

def shopping_meet(request):
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

def communaute(request) :
        return render(request, 'communaute.html', {})
#-------------------telephone----------------

def communaute_telephone(request) :
        sujets = Sujet_telephone.objects.all()
        return render(request, 'communaute_telephone.html', {'sujets': sujets})


def creer_sujet_telephone(request):
    if request.method == 'POST':
        form = Sujet_telephoneForm(request.POST)
        if form.is_valid():
            sujet_telephone = form.save(commit=False)
            sujet_telephone.auteur = request.user  # Associez l'utilisateur actuellement connecté en tant qu'auteur
            sujet_telephone.save()
            return redirect('communaute_telephone')
    else:
        form = Sujet_telephoneForm()
    return render(request, 'creer_sujet_telephone.html', {'form': form})

def details_sujet_telephone(request, sujet_telephone_id):
    sujet_telephone = Sujet_telephone.objects.get(id=sujet_telephone_id)
    commentaires = sujet_telephone.commentaires.all()  # Utilisez 'commentaires' ici

    if request.method == 'POST':
        form = Commentaire_telephoneForm(request.POST)
        if form.is_valid():
            commentaire_telephone = form.save(commit=False)
            commentaire_telephone.sujet_telephone = sujet_telephone
            commentaire_telephone.auteur = request.user
            commentaire_telephone.save()
            return redirect('details_sujet_telephone', sujet_telephone_id=sujet_telephone.id)
    else:
        form = Commentaire_telephoneForm()

    return render(request, 'details_sujet_telephone.html', {'sujet_telephone': sujet_telephone, 'commentaires': commentaires, 'form': form})

def supprimer_sujet_telephone(request, sujet_telephone_id):
    sujet_telephone = get_object_or_404(Sujet_telephone, id=sujet_telephone_id)
    if request.user == sujet_telephone.auteur:
        sujet_telephone.delete()
    return redirect('communaute_telephone')
#--------Tablette------------------

def communaute_tablette(request) :
        sujets = Sujet_tablette.objects.all()
        return render(request, 'communaute_tablette.html', {'sujets': sujets})


def creer_sujet_tablette(request):
    if request.method == 'POST':
        form = Sujet_tabletteForm(request.POST)
        if form.is_valid():
            sujet_tablette = form.save(commit=False)
            sujet_tablette.auteur = request.user  # Associez l'utilisateur actuellement connecté en tant qu'auteur
            sujet_tablette.save()
            return redirect('communaute_tablette')
    else:
        form = Sujet_tabletteForm()
    return render(request, 'creer_sujet_tablette.html', {'form': form})

def details_sujet_tablette(request, sujet_tablette_id):
    sujet_tablette = Sujet_tablette.objects.get(id=sujet_tablette_id)
    commentaires = sujet_tablette.commentaires.all()  # Utilisez 'commentaires' ici

    if request.method == 'POST':
        form = Commentaire_tabletteForm(request.POST)
        if form.is_valid():
            commentaire_tablette = form.save(commit=False)
            commentaire_tablette.sujet_tablette = sujet_tablette
            commentaire_tablette.auteur = request.user
            commentaire_tablette.save()
            return redirect('details_sujet_tablette', sujet_tablette_id=sujet_tablette.id)
    else:
        form = Commentaire_tabletteForm()

    return render(request, 'details_sujet_tablette.html', {'sujet_tablette': sujet_tablette, 'commentaires': commentaires, 'form': form})

def supprimer_sujet_tablette(request, sujet_tablette_id):
    sujet_tablette = get_object_or_404(Sujet_tablette, id=sujet_tablette_id)
    if request.user == sujet_tablette.auteur:
        sujet_tablette.delete()
    return redirect('communaute_tablette')


#--------ordinateur -----------------

def communaute_ordinateur(request) :
        sujets = Sujet_ordinateur.objects.all()
        return render(request, 'communaute_ordinateur.html', {'sujets': sujets})


def creer_sujet_ordinateur(request):
    if request.method == 'POST':
        form = Sujet_ordinateurForm(request.POST)
        if form.is_valid():
            sujet_ordinateur = form.save(commit=False)
            sujet_ordinateur.auteur = request.user  # Associez l'utilisateur actuellement connecté en tant qu'auteur
            sujet_ordinateur.save()
            return redirect('communaute_ordinateur')
    else:
        form = Sujet_ordinateurForm()
    return render(request, 'creer_sujet_ordinateur.html', {'form': form})

def details_sujet_ordinateur(request, sujet_ordinateur_id):
    sujet_ordinateur = Sujet_ordinateur.objects.get(id=sujet_ordinateur_id)
    commentaires = sujet_ordinateur.commentaires.all()  # Utilisez 'commentaires' ici

    if request.method == 'POST':
        form = Commentaire_ordinateurForm(request.POST)
        if form.is_valid():
            commentaire_ordinateur = form.save(commit=False)
            commentaire_ordinateur.sujet_ordinateur = sujet_ordinateur
            commentaire_ordinateur.auteur = request.user
            commentaire_ordinateur.save()
            return redirect('details_sujet_ordinateur', sujet_ordinateur_id=sujet_ordinateur.id)
    else:
        form = Commentaire_ordinateurForm()

    return render(request, 'details_sujet_ordinateur.html', {'sujet_ordinateur': sujet_ordinateur, 'commentaires': commentaires, 'form': form})

def supprimer_sujet_ordinateur(request, sujet_ordinateur_id):
    sujet_ordinateur = get_object_or_404(Sujet_ordinateur, id=sujet_ordinateur_id)
    if request.user == sujet_ordinateur.auteur:
        sujet_ordinateur.delete()
    return redirect('communaute_ordinateur')



#--------Accessoire_telephone------------------

def communaute_Accessoire_telephone(request) :
        sujets = Sujet_Accessoire_telephone.objects.all()
        return render(request, 'communaute_Accessoire_telephone.html', {'sujets': sujets})


def creer_sujet_Accessoire_telephone(request):
    if request.method == 'POST':
        form = Sujet_Accessoire_telephoneForm(request.POST)
        if form.is_valid():
            sujet_Accessoire_telephone = form.save(commit=False)
            sujet_Accessoire_telephone.auteur = request.user  # Associez l'utilisateur actuellement connecté en tant qu'auteur
            sujet_Accessoire_telephone.save()
            return redirect('communaute_Accessoire_telephone')
    else:
        form = Sujet_Accessoire_telephoneForm()
    return render(request, 'creer_sujet_Accessoire_telephone.html', {'form': form})

def details_sujet_Accessoire_telephone(request, sujet_Accessoire_telephone_id):
    sujet_Accessoire_telephone = Sujet_Accessoire_telephone.objects.get(id=sujet_Accessoire_telephone_id)
    commentaires = sujet_Accessoire_telephone.commentaires.all()  # Utilisez 'commentaires' ici

    if request.method == 'POST':
        form = Commentaire_Accessoire_telephoneForm(request.POST)
        if form.is_valid():
            commentaire_Accessoire_telephone = form.save(commit=False)
            commentaire_Accessoire_telephone.sujet_Accessoire_telephone = sujet_Accessoire_telephone
            commentaire_Accessoire_telephone.auteur = request.user
            commentaire_Accessoire_telephone.save()
            return redirect('details_sujet_Accessoire_telephone', sujet_Accessoire_telephone_id=sujet_Accessoire_telephone.id)
    else:
        form = Commentaire_Accessoire_telephoneForm()

    return render(request, 'details_sujet_Accessoire_telephone.html', {'sujet_Accessoire_telephone': sujet_Accessoire_telephone, 'commentaires': commentaires, 'form': form})

def supprimer_sujet_Accessoire_telephone(request, sujet_Accessoire_telephone_id):
    sujet_Accessoire_telephone = get_object_or_404(Sujet_Accessoire_telephone, id=sujet_Accessoire_telephone_id)
    if request.user == sujet_Accessoire_telephone.auteur:
        sujet_Accessoire_telephone.delete()
    return redirect('communaute_Accessoire_telephone')



#--------Accessoire_tablette------------------

def communaute_Accessoire_tablette(request) :
        sujets = Sujet_Accessoire_tablette.objects.all()
        return render(request, 'communaute_Accessoire_tablette.html', {'sujets': sujets})


def creer_sujet_Accessoire_tablette(request):
    if request.method == 'POST':
        form = Sujet_Accessoire_tabletteForm(request.POST)
        if form.is_valid():
            sujet_Accessoire_tablette = form.save(commit=False)
            sujet_Accessoire_tablette.auteur = request.user  # Associez l'utilisateur actuellement connecté en tant qu'auteur
            sujet_Accessoire_tablette.save()
            return redirect('communaute_Accessoire_tablette')
    else:
        form = Sujet_Accessoire_tabletteForm()
    return render(request, 'creer_sujet_Accessoire_tablette.html', {'form': form})

def details_sujet_Accessoire_tablette(request, sujet_Accessoire_tablette_id):
    sujet_Accessoire_tablette = Sujet_Accessoire_tablette.objects.get(id=sujet_Accessoire_tablette_id)
    commentaires = sujet_Accessoire_tablette.commentaires.all()  # Utilisez 'commentaires' ici

    if request.method == 'POST':
        form = Commentaire_Accessoire_tabletteForm(request.POST)
        if form.is_valid():
            commentaire_Accessoire_tablette = form.save(commit=False)
            commentaire_Accessoire_tablette.sujet_Accessoire_tablette = sujet_Accessoire_tablette
            commentaire_Accessoire_tablette.auteur = request.user
            commentaire_Accessoire_tablette.save()
            return redirect('details_sujet_Accessoire_tablette', sujet_Accessoire_tablette_id=sujet_Accessoire_tablette.id)
    else:
        form = Commentaire_Accessoire_tabletteForm()

    return render(request, 'details_sujet_Accessoire_tablette.html', {'sujet_Accessoire_tablette': sujet_Accessoire_tablette, 'commentaires': commentaires, 'form': form})

def supprimer_sujet_Accessoire_tablette(request, sujet_Accessoire_tablette_id):
    sujet_Accessoire_tablette = get_object_or_404(Sujet_Accessoire_tablette, id=sujet_Accessoire_tablette_id)
    if request.user == sujet_Accessoire_tablette.auteur:
        sujet_Accessoire_tablette.delete()
    return redirect('communaute_Accessoire_tablette')


#--------Accessoire_ordinateur------------------

def communaute_Accessoire_ordinateur(request) :
        sujets = Sujet_Accessoire_ordinateur.objects.all()
        return render(request, 'communaute_Accessoire_ordinateur.html', {'sujets': sujets})


def creer_sujet_Accessoire_ordinateur(request):
    if request.method == 'POST':
        form = Sujet_Accessoire_ordinateurForm(request.POST)
        if form.is_valid():
            sujet_Accessoire_ordinateur = form.save(commit=False)
            sujet_Accessoire_ordinateur.auteur = request.user  # Associez l'utilisateur actuellement connecté en tant qu'auteur
            sujet_Accessoire_ordinateur.save()
            return redirect('communaute_Accessoire_ordinateur')
    else:
        form = Sujet_Accessoire_ordinateurForm()
    return render(request, 'creer_sujet_Accessoire_ordinateur.html', {'form': form})

def details_sujet_Accessoire_ordinateur(request, sujet_Accessoire_ordinateur_id):
    sujet_Accessoire_ordinateur = Sujet_Accessoire_ordinateur.objects.get(id=sujet_Accessoire_ordinateur_id)
    commentaires = sujet_Accessoire_ordinateur.commentaires.all()  # Utilisez 'commentaires' ici

    if request.method == 'POST':
        form = Commentaire_Accessoire_ordinateurForm(request.POST)
        if form.is_valid():
            commentaire_Accessoire_ordinateur = form.save(commit=False)
            commentaire_Accessoire_ordinateur.sujet_Accessoire_ordinateur = sujet_Accessoire_ordinateur
            commentaire_Accessoire_ordinateur.auteur = request.user
            commentaire_Accessoire_ordinateur.save()
            return redirect('details_sujet_Accessoire_ordinateur', sujet_Accessoire_ordinateur_id=sujet_Accessoire_ordinateur.id)
    else:
        form = Commentaire_Accessoire_ordinateurForm()

    return render(request, 'details_sujet_Accessoire_ordinateur.html', {'sujet_Accessoire_ordinateur': sujet_Accessoire_ordinateur, 'commentaires': commentaires, 'form': form})

def supprimer_sujet_Accessoire_ordinateur(request, sujet_Accessoire_ordinateur_id):
    sujet_Accessoire_ordinateur = get_object_or_404(Sujet_Accessoire_ordinateur, id=sujet_Accessoire_ordinateur_id)
    if request.user == sujet_Accessoire_ordinateur.auteur:
        sujet_Accessoire_ordinateur.delete()
    return redirect('communaute_Accessoire_ordinateur')
