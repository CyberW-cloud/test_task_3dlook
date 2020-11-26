from django.db.models import F
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from product_api.models import Product
from product_api.api.serializers import ProductSerializer


@api_view(['GET', ])
def api_detail_product_view(request, uuid):
    product = get_object_or_404(Product.objects.all(), uuid=uuid)
    serializer = ProductSerializer(product)

    return Response(serializer.data)


class ApiAllProductsView(ListAPIView):
    queryset = Product.objects.all()
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

        return queryset
