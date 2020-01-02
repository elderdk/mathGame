from django.db import models

# Create your models here.
class Settings(models.Model):
    num1Max = models.IntegerField()
    num2Max = models.IntegerField()
    add = models.BooleanField()
    subtract = models.BooleanField()
    multiply = models.BooleanField()
    divide = models.BooleanField()