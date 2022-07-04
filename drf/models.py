from distutils.command.upload import upload
from email.mime import image
from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.00)
    image = models.ImageField(blank=True, null=True, upload_to="products")
    stock = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product_name