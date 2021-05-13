from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=60)
    designation = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name