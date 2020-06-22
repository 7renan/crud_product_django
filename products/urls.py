from django.urls import path

# views
from . import views


app_name='products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
]