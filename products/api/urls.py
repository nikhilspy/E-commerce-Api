from django.urls import path
from .views import list_all_products, create_product, view_product, purchase_product, add_review, get_all_review, delete_product, rate_product

urlpatterns = [
    path("pts/products", list_all_products, name='all-items' ),
    path("pts/products/create", create_product, name='create-item' ),
    path('pts/products/<int:pk>', view_product, name='view-product' ),
    path('pts/products/purchase', purchase_product, name='add-prod'),
    path('pts/products/review', add_review, name='add-review'),
    path('pts/products/<int:pk>/reviews', get_all_review, name='all-review'),
    path('pts/deleteProduct/<int:pk>', delete_product, name = 'del-product'),
    path('pts/products/rate', rate_product, name = 'rate'),

]