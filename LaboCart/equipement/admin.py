from django.contrib import admin
from equipement.models import Equipement, DocEquipement, Matrice

class EquipementAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('Appareil', 'Code_machine', 'numero_serie','Emplacement', 'Num') # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Equipement, EquipementAdmin)
admin.site.register(DocEquipement)
admin.site.register(Matrice)
