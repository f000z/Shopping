from django.db import models
from user.models import Profile
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quanity = models.IntegerField(default=1)


    def __str__(self):
        return str(self.user.user.first_name)
    