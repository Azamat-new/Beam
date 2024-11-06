from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.ProductImageListCreate.as_view(), name='productimage-list-create'),
    path('images/<int:pk>/', views.ProductImageDetail.as_view(), name='productimage-detail'),
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('orders/', views.OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
]
