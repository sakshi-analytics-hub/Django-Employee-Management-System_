

# Create your models here.

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name
