from django.contrib import admin

from .models import Client
from .models import Lunette
from .models import Commande

admin.site.register(Client)
admin.site.register(Lunette)
admin.site.register(Commande)

# Register your models here.
