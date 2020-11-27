from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from product_api.models import Product


class ProductViewAPITestCase(APITestCase):

    def setUp(self):
        logo = Image.new('RGB', (60, 30), color='red')
        logo.save('test_image.jpg')
        logo = SimpleUploadedFile(name='test_image.jpg',
                                  content=open('test_image.jpg', 'rb').read(),
                                  content_type='image/jpeg')
        Product.objects.create(name="Test name", description="test description", logo=logo)
        return super().setUp()

    def test_post_positive(self):
        logo = SimpleUploadedFile(name='test_image.jpg',
                                  content=open('test_image.jpg', 'rb').read(),
                                  content_type='image/jpeg')
        data = {
            "name": "Test name",
            "description": "Test description",
            "logo": logo
        }
        response = self.client.post("/api/products/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_missing_data(self):
        data = {
            "description": "Sample description",
            "logo": "picture.jpg"
        }
        response = self.client.post("/api/products/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_invalid_data(self):
        data = {
            "name": 123,
            "description": "Test description",
            "logo": 123
        }
        response = self.client.post("/api/products/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_positive(self):
        data = {
            "description": "Edited description"
        }
        uuid = Product.objects.get(name="Test name").uuid
        response = self.client.put(f'/api/products/{uuid}/update', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_already_modified(self):
        data = {
            "description": "Test description",
        }
        uuid = Product.objects.get(name="Test name").uuid
        # For the second time will be refused
        response = self.client.put(f'/api/products/{uuid}/update', data)
        response = self.client.put(f'/api/products/{uuid}/update', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_invalid_uuid(self):
        data = {
            "description": "Test description",
        }
        uuid = 'random_string'
        response = self.client.put(f'/api/products/{uuid}/update', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_positive(self):
        uuid = Product.objects.get(name="Test name").uuid
        response = self.client.delete(f'/api/products/{uuid}/delete')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_negative(self):
        uuid = 'random_string'
        response = self.client.delete(f'/api/products/{uuid}/delete')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
