from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    nutrition = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)
    product_image = models.CharField(max_length=1000)

    class Meta: 
        unique_together = ['name','origin']
        