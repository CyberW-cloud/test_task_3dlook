import uuid

from django.db import models
from django.core.files import File

from product_api.utilities.utils import upload_location, rotate_logo


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
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.uuid}'


    # def save(self, *args, **kwargs):
        #     if self.logo:
        #         base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #         dir_path = os.path.normpath('images/product/')
        #         filename = os.path.normpath(self.logo.url)
        #         full_path = os.path.join(base_dir, dir_path) + filename
        #         print('full_path', full_path)
        #
        #         self.rotate_duration = rotate_logo(self.logo.url)
        #     super(Product, self).save(*args, **kwargs)