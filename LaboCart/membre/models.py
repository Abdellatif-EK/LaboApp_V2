from django.db import models
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.core.validators import MaxValueValidator, MinValueValidator

class Utilisateur(models.Model):
    user_id = models.fields.AutoField(primary_key=True)
    first_name = models.fields.CharField(max_length=100, null=False)
    last_name = models.fields.CharField(max_length=100, null=False)
    email = models.fields.EmailField(max_length=100, null=False)
    password = models.fields.CharField(max_length=100, null=False)
    phone = models.fields.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Analyste(models.Model):
    user_id = models.fields.AutoField(primary_key=True)
    first_name = models.fields.CharField(max_length=100, null=False)
    last_name = models.fields.CharField(max_length=100, null=False)
    email = models.fields.EmailField(max_length=100, null=False)
    password = models.fields.CharField(max_length=100, null=False)
    phone = models.fields.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    