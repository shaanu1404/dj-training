from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('get_single_product', kwargs={'id': self.id})

    def get_doubled_price(self):
        return 2 * self.price


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
