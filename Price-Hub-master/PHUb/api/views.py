from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Phone

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
def telephones(request):
    phones = Phone.objects.all()
    return render(request, 'telephones.html', {'phones': phones})