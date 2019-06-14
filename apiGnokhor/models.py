from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    image = models.FileField(upload_to='post_image', blank=True)

 #image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.prenom

class Lunette(models.Model):
    nom = models.CharField(max_length=200)
    typelunette = models.CharField(max_length=200)
    prix = models.CharField(max_length=200)
    photo = models.FileField(upload_to='post_image', blank=True)

 #image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.nom

# Create your models here.
