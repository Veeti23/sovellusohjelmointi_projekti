from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Product model to store product name, price and date added
class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Lisää tuotteen nimi")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Lisää tuotteen hinta")
    stock = models.PositiveIntegerField(default=0, help_text="Lisää tuotteen varastomäärä")
    image = models.ImageField(upload_to="images/", blank=True, null=True, help_text="Lisää tuotekuva")
    date_added = models.DateTimeField(auto_now_add=True)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="Alennushinta")

    def is_in_stock(self):
        return self.stock > 0

    def get_discount_percent(self):
        if self.discount_price:
            return int(100 - (self.discount_price / self.price * 100))
        return 0

    def __str__(self):
        return (f"{self.name}: {self.price}€")


# Productdetail model to store product details and photo
class Productdetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail = models.CharField(max_length=400, help_text="Lisää tuotteen tarkempi kuvaus")
    photo = models.ImageField(upload_to="images/", blank=True, null=True, help_text="Lisää tuotekuva")

    def __str__(self):
        return (f"{self.product.name}: {self.product.price}€ Tuotekuvaus: {self.detail}")


# Review model to store product reviews
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=300)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], help_text="Anna tähtiä (0-5)")
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.product}: {str(self.stars)} stars {self.review}")


# Cart model to store shopping cart details
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_cost() for item in self.cartitem_set.all())


# CartItem model to store items in the cart
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def get_cost(self):
        if self.product.discount_price:
            return self.product.discount_price * self.quantity
        return self.product.price * self.quantity