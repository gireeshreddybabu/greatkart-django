from django.http.response import HttpResponse
from carts.models import CartItem
from django.core.checks.messages import Error
from store.models import Product
from django.shortcuts import get_object_or_404, render
from .models import Category
from carts.views import _cart_id
# Create your views here.

def store(request, category_slug = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count' : product_count,

    }
    return render(request,'store/store.html', context)


def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product = single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart' : in_cart,
    }
    return render(request,'store/product_details.html', context)