import logging

from django.db.models import F
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from product_api.models import Product
from product_api.api.serializers import ProductSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
def api_detail_product_view(request, uuid):
    product = get_object_or_404(Product.objects.all(), uuid=uuid)
    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['POST'])
def api_create_product_view(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Logger in model.py
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_update_product_view(request, uuid):
    # Check if the product not yet modified
    product = get_object_or_404(Product.objects.all(), uuid=uuid, updated=F('created'))
    serializer = ProductSerializer(instance=product, data=request.data, partial=True)

    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'update successful'
        return Response(data=data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_product_view(request, uuid):
    product = get_object_or_404(Product.objects.all(), uuid=uuid)
    operation = product.delete()

    data = {}
    if operation:
        data['success'] = 'delete successful'
        logger.info(f'{product.name} - {product.uuid} deleted from DB')
    else:
        data['failure'] = 'delete failed'
        logger.warning(f'{product.name} - {product.uuid} failed to delete from DB')

    return Response(data=data, status=status.HTTP_200_OK)


class ApiAllProductsView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """
        Optionally restricts non-modified products
        by excluding using `modified` query parameter in the URL.
        """
        queryset = Product.objects.all()
        modified = self.request.query_params.get('modified', None)

        if modified == "true":
            queryset = queryset.exclude(updated=F('created'))
        elif modified == "false":
            queryset = queryset.filter(updated=F('created'))

        return queryset
