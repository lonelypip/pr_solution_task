from django.db import models
from django.contrib.auth.models import User



class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.DateField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
