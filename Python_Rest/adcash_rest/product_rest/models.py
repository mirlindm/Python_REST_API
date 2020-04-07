from django.db import models
from django.contrib import admin


class Category(models.Model):
    #category_id = models.IntegerField()
    category_name = models.CharField(max_length=25)
    category_description = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    #product_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    product_amount = models.IntegerField()

    def __str__(self):
        return self.product_name

