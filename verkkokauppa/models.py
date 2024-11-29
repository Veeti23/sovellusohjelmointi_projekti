from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}€"

# Reviews model.
class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        help_text="Give a rating between 1-5",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['date']

    def __str__(self):
        return str(self.rating)

# Product Description model.
class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.product.name}, {self.description}"

    class Meta:
        verbose_name = "Product Description"
        verbose_name_plural = "Product Descriptions"
        ordering = ['product']

