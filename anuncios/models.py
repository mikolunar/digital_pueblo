from django.db import models

# Create your models here.


class Anuncio(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
