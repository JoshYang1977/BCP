from django.db import models
from django.db.models import CharField, ForeignKey

# Create your models here.
class scenario(models.Model):
    color = CharField(max_length=10)

    def __str__(self):
        return self.color

class department(models.Model):
    name = CharField(max_length=3)

    def __str__(self):
        return self.name

class bcp_measure(models.Model):
    measure = CharField(max_length=100)
    color = ForeignKey(scenario, on_delete=models.SET_NULL,null=True)
    name = ForeignKey(department, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.measure
