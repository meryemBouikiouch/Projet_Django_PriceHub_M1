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
from .forms import AdvancedSearchForm

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

    # Créer le contexte
    context = {'phones': phones, 'query': query, 'sort_option': sort_option, 'advanced_search_form': advanced_search_form}

    # Rendre le modèle avec le contexte
    return render(request, 'telephones.html', context)
def phone_detail(request, phone_id):
    phone = get_object_or_404(Phone, identifiant=phone_id)
    context = {'phone': phone}
    return render(request, 'phone_detail.html', context)