from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ("-id",)

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name
