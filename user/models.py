from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.phone_number} {self.address} {self.age}"



