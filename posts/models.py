"""Posts models."""

# Django
from django.db import models


class User(models.Model):
    """User model."""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Este nos permite agregar mucho mas texto y ademas puede estar vacia.
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)
    #Cuando se cree una instancia de esta tabla en la base de datos, le cargara la fecha en que se creo
    created = models.DateTimeField(auto_now_add=True)
    # Guardara la fecha en que se edito por ultima vez 
    modified = models.DateTimeField(auto_now=True)
