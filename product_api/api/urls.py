from django.urls import path

from product_api.api.views import (
    api_detail_product_view,
    api_create_product_view,
    api_update_product_view,
    api_delete_product_view,
    ApiAllProductsView,
)

app_name = 'product_api'

urlpatterns = [
    path('<uuid>', api_detail_product_view, name='product_detail'),
    path('create/', api_create_product_view, name='products_create'),
    path('<uuid>/update', api_update_product_view, name='products_update'),
    path('<uuid>/delete', api_delete_product_view, name='products_delete'),
    path('', ApiAllProductsView.as_view(), name='products_all'),
]