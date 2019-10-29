from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    nutrition = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)
    product_image = models.CharField(max_length=1000)

    objects = models.Manager()

    class Meta: 
        unique_together = ['name','origin']

def create_process(_name, _price, _nutrition, _origin, _product_image):
    product = Product(name=_name, price=_price, nutrition=_nutrition, origin=_origin, product_image=_product_image)

    # Validation - Ensure the instance values comply with those of the model definition
    # Rasie ValidationError if the test failed
    product.full_clean()
    
    # Create the record in the target database
    product.save()

def fetch_all_products_process():
    # Return a dict of product
    return Product.objects.in_bulk()