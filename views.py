
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(product=product, quantity=1)
    return redirect('cart')

def cart(request):
    orders = Order.objects.all()
    return render(request, 'shop/cart.html', {'orders': orders})
