from django.urls import path

# views
from . import views


app_name='products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk_product>/', views.product_update, name='product_update'),
    path('delete/<int:pk_product>/', views.product_delete, name='product_delete'),
]