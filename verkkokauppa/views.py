from django.shortcuts import render, get_object_or_404
from .models import Product, Productdetail, Review


def home(request):
    # Render the home page
    return render(request, "verkkokauppa/home.html")


def products(request):
    # Render the products page
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "verkkokauppa/products.html", context)


def product_detail(request, product_id):
    # Render the product detail page
    product = get_object_or_404(Product, id=product_id)
    productdetails = Productdetail.objects.filter(product=product)
    context = {"product": product, "productdetails": productdetails}
    return render(request, "verkkokauppa/product.html", context)


def review(request, product_id):
    # Render the review page
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product, "reviews": product.review_set.all()}
    return render(request, "verkkokauppa/review.html", context)