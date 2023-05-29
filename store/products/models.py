from django.db import models
import os
def get_path_file(instance, filename):
    category = instance.category.name
    name = instance.name
    return os.path.join('productImg', category, name, filename)

# id by default
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=get_path_file)  # products_images
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f"Продукт: {self.name} | Категория {self.category.name}"
