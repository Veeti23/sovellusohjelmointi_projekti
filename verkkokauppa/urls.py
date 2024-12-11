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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)