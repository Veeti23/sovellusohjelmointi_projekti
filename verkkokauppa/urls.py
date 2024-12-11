from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    # Info page
    path("info/", views.info, name="info"),
    # Search products page
    path("search/", views.search_products, name="search_products"),
    # Cart pages
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)