from django.urls import path
from . import views

app_name = "verkkokauppa"

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Products page
    path("products", views.products, name="products"),
    # Product review page
    path("review/<int:product_id>/", views.review, name="review"),
    # Product detail page
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    # Add review page
    path("product/<int:product_id>/add_review/", views.add_review, name="add_review"),
   
]