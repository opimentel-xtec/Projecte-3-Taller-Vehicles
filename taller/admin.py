from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(Article)
admin.site.register(OrdreReparacio)
admin.site.register(OrdreReparacioArticle)