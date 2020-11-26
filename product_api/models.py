import uuid
from django.db import models


def upload_location(instance, filename, **kwargs):
    file_path = f'images/product/{filename}'
    return file_path


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    logo = models.ImageField(upload_to=upload_location, null=False, blank=False)
    rotate_duration = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.uuid}'
