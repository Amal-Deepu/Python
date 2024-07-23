from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pics', null=True)
    category = models.CharField(max_length=250)
    languages = models.CharField(max_length=250)
    actors = models.CharField(max_length=250, null=True)
    year = models.DateField()
    link = models.CharField(max_length=250, default=None, null=True)
    rating = models.FloatField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



