from django.db import models
from datetime import datetime

# Corrected usage
date_obj = datetime.fromisoformat("2022-01-01")

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name

