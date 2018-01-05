from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    color = models.CharField(max_length=50)
    price = models.IntegerField()
    img_link = models.CharField(max_length=2000)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name + '-' + self.color


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name