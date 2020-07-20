from django.db import models

# Create your models here.
class Countermodel(models.Model):
    number = models.CharField(max_length = 10)