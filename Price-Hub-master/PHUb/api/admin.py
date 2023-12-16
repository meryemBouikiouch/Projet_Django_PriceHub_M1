from django.contrib import admin
from .models import HistoriqueVisite
from .models import Souhaits
from .models import *

admin.site.register(HistoriqueVisite)
admin.site.register(Souhaits)
admin.site.register(Meeting)

admin.site.register(Commentaire_telephone)
admin.site.register(Sujet_telephone)

admin.site.register(Commentaire_tablette)
admin.site.register(Sujet_tablette)

admin.site.register(Commentaire_ordinateur)
admin.site.register(Sujet_ordinateur)

admin.site.register(Commentaire_Accessoire_telephone)
admin.site.register(Sujet_Accessoire_telephone)


admin.site.register(Commentaire_Accessoire_tablette)
admin.site.register(Sujet_Accessoire_tablette)

admin.site.register(Commentaire_Accessoire_ordinateur)
admin.site.register(Sujet_Accessoire_ordinateur)
# Register your models here.
