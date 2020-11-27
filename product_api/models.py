import logging
import uuid

from django.db import models
from django.core.files import File

from product_api.utilities.utils import upload_location, rotate_logo

logger = logging.getLogger(__name__)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    logo = models.ImageField(upload_to=upload_location, null=False, blank=False)
    rotate_duration = models.FloatField()

    def save(self, *args, **kwargs):
        if self.logo:
            output, rotate_duration = rotate_logo(self.logo)
            self.logo = File(output, self.logo.name)
            self.rotate_duration = rotate_duration
        logger.info(f'{self.name} - {self.uuid} saved to DB')
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.uuid}'
