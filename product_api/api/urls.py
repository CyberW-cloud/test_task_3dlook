from django.urls import path

from product_api.api.views import api_detail_product_view, ApiAllProductsView

app_name = 'product_api'

urlpatterns = [
    path('<uuid>', api_detail_product_view, name='product_detail'),
    path('', ApiAllProductsView.as_view(), name='products_all'),
]