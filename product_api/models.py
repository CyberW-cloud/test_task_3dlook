import uuid
from django.db import models


def upload_location(instance, **kwargs):
    file_path = f'images/product/{instance.name}'
    return file_path


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated = models.DateTimeField(default=None, verbose_name="Date updated")
    logo = models.ImageField(upload_to=upload_location, null=False, blank=False)
    rotate_duration = models.FloatField(null=False, blank=False)