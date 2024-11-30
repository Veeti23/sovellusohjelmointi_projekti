from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Productdetail, Review
from .forms import ReviewForm


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

def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect("verkkokauppa:review", product_id=product.id)
    else:
        form = ReviewForm()
    context = {"product": product, "form": form}
    return render(request, "verkkokauppa/add_review.html", context)