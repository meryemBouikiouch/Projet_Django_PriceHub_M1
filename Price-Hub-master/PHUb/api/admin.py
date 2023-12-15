from django.contrib import admin
from .models import HistoriqueVisite
from .models import Souhaits
from .models import *

admin.site.register(HistoriqueVisite)
admin.site.register(Souhaits)
admin.site.register(Meeting)


# Register your models here.
