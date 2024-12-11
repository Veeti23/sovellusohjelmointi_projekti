from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Productdetail, Cart, CartItem
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    # Render the home page.
    return render(request, "verkkokauppa/home.html")


def products(request):
    # Get all products
    products = Product.objects.all()
    context = {
        "products": products,
    }
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
    productdetails = Productdetail.objects.filter(product=product)
    context = {"product": product, "productdetails": productdetails, "reviews": product.review_set.all()}
    return render(request, "verkkokauppa/product.html", context)

@login_required
def add_review(request, product_id):
    # Add a new review for a product.
    product = get_object_or_404(Product, id=product_id)
    # Check if the form has been submitted.
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
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

def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query))
    context = {"products": products, "query": query}
    return render(request, "verkkokauppa/search_results.html", context)

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'verkkokauppa/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('verkkokauppa:view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('verkkokauppa:view_cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0 and quantity <= cart_item.product.stock:
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('verkkokauppa:view_cart')