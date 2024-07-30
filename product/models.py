from django.db import models

# Create your models here.


class Size(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    
    def str(self):
        return self.name
    

class WarehouseItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.ManyToManyField(Color)
    description = models.TextField()
    size = models.ManyToManyField(Size)
    quantity = models.IntegerField(default=1)
    
    def str(self):
        return self.name
    

class ProductImage(models.Model):
    photo = models.ImageField(upload_to='product/')
    warehouse_item = models.ForeignKey(WarehouseItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    warehouse_item = models.ForeignKey(WarehouseItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def str(self):
        return self.name
