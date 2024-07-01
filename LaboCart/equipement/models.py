from django.db import models
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.core.validators import MaxValueValidator, MinValueValidator

class Equipement(models.Model):
    Num = models.fields.IntegerField(null=False) # c'est important ce numéro. C'est lui qui permet d'identifier un équipement au niveau du site
    Emplacement = models.fields.CharField(max_length=100,null=True)
    Appareil = models.fields.CharField(max_length=100,null=False)
    Etat = models.fields.CharField(max_length=100,null=True)
    modele = models.fields.CharField(max_length=100, null=True)
    Code_machine = models.fields.CharField(max_length=20, null=True)
    Password = models.fields.CharField(max_length=20, null=True)
    matrcie_acces = models.fields.CharField(max_length=100, null=True)
    Sauvegarde = models.fields.CharField(max_length=100, null=True)
    Connecte_reseau = models.fields.CharField(max_length=100, null=True)
    Connecte_AD = models.fields.CharField(max_length=100, null=True)
    connecté_imprimante = models.fields.CharField(max_length=10, null=True)
    Maintenance = models.fields.CharField(max_length=100, null=True)
    planning_sauvegarde = models.fields.CharField(max_length=100, null=True)
    Logiciel = models.fields.CharField(max_length=100, null=True)
    version_logiciel = models.fields.CharField(max_length=100, null=True)
    date_installation = models.fields.CharField(max_length=100, null=True)
    Version_windows= models.fields.CharField(max_length=100, null=True)
    Situation = models.fields.CharField(max_length=100, null=True)
    Fournisseur = models.fields.CharField(max_length=100, null=True)
    Etat_materiel_informatique= models.fields.CharField(max_length=100, null=True)
    numero_serie= models.fields.CharField(max_length=40, null=True)
    Documentation = models.fields.CharField(max_length=100,null=True)
    DOC_qualification = models.fields.CharField(max_length=100,null=True)
    QX =  models.fields.CharField(max_length=20, null=True)
    description = models.fields.CharField(max_length=1000, null=True)
    site_officiel = models.fields.URLField(null=True,blank=True)
    Autres = models.fields.CharField(max_length=100, null=True)
 
    def __str__(self):
        return f'{self.Code_machine} modèle {self.modele}'

# Dans le modèle ci-aprsè j'associe une image et un fichier à un équipement. De tel sorte que l'on puisse enregistrer plusieurs images et fichiers à un équipement.
# On aurait pu ajour image et pdf dans le modèle images mais on serait limité à une et une seule image et un seul fichier. Le nom vient du fait qu'à la base je ne voulais qu'ajouter des images.
class DocEquipement(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='fichiers/', blank=True, null=True)
    def __str__(self):
        return f'Image {self.id} - Equipement: {self.equipement.Code_machine}'
 
class Matrice(models.Model):
    class status(models.TextChoices):
        Actif = 'actif'
        Inactive = 'Inactif'
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, related_name='matrice')
    login = models.fields.CharField(max_length=100, null=True)
    Nom = models.fields.CharField(max_length=100, null=True)
    Prenom = models.fields.CharField(max_length=100, null=True)
    Role = models.fields.CharField(max_length=200, null=True)
    Situation = models.fields.CharField(choices=status.choices, max_length=20)
    date_modfication = models.fields.DateField(auto_now=True)

