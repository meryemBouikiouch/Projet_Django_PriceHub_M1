
from django.urls import  path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('log_in/',log_in,name='log_in'),
    path('signup/',sign_up,name='sign_up'),
    path('logout/',logout,name='logout'),
    path('home/',home,name='home'),
    path('telephones/',telephones,name='telephones'),
    
]