from django.db import models


# Create your models here.


class Main_view(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=300, default='new collection', null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} + {self.title}"
