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


def product_update(request, pk_product):
    product = Product.objects.get(pk=pk_product)
    context = {
        'product':product,
    }

    if request.method == 'POST':
        new_name = request.POST['name']
        new_price = request.POST['price']
        new_category = request.POST['category']

        product.name = new_name
        product.price = new_price
        product.category = new_category
        product.save()

        return redirect('products:product_list')

    return render(request, 'product_update.html', context)


def product_delete(request, pk_product):
    product = Product.objects.get(pk=pk_product)
    product.delete()
    return redirect('products:product_list')