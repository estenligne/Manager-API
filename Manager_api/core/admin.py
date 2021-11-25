from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register(Projet)
admin.site.register(Tache)
admin.site.register(Relation_taches)
admin.site.register(Employe)
admin.site.register(Rapport_employe)
admin.site.register(Suivre)
admin.site.register(Commentaires)