from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Productdetail
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def home(request):
    # Render the home page.
    return render(request, "verkkokauppa/home.html")


def products(request):
    # Render the products page.
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "verkkokauppa/products.html", context)


def product_detail(request, product_id):
    # Render the product detail page.
    product = get_object_or_404(Product, id=product_id)
    # Get the product details for the product.
    productdetails = Productdetail.objects.filter(product=product)
    context = {"product": product, "productdetails": productdetails}
    return render(request, "verkkokauppa/product.html", context)

def review(request, product_id):
    # Render the review page.
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product, "reviews": product.review_set.all()}
    return render(request, "verkkokauppa/product.html", context)

@login_required
def add_review(request, product_id):
    # Add a new review for a product.
    product = get_object_or_404(Product, id=product_id)
    # Check if the form has been submitted.
    if request.method == "POST":
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            # Save the review to the database.
            review = form.save(commit=False)
            # Set the product for the review.
            review.product = product
            # Set the user for the review.
            review.save()
            return redirect("verkkokauppa:review", product_id=product.id)
    else:
        # Create a new form.
        form = ReviewForm()

    context = {"product": product, "form": form}
    return render(request, "verkkokauppa/add_review.html", context)


def info(request):
    # Render the info page.
    return render(request, "verkkokauppa/info.html")