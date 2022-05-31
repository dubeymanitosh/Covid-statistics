from django.db import models
# Create your models here.
class Poster(models.Model):
    poster=models.ImageField(upload_to="")