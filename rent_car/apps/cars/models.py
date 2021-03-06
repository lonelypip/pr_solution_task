from django.db import models
from django.contrib.auth.models import User



class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.DateField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} клиента {self.owner}, {self.year} года'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
