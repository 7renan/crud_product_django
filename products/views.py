from django.shortcuts import render, redirect

# models
from products.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'product_list.html', context)


def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']

        Product.objects.create(
            name=name,
            price=price,
            category=category,
        )
        return redirect('products:product_list')
    return render(request, 'product_create.html')