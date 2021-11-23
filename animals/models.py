from django.db import models
# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=200)
    legs = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    family = models.ForeignKey('family.Family', on_delete=models.CASCADE)


