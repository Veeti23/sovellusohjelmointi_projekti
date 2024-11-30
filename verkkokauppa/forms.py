from django import forms
from .models import Product, Productdetail, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review", "stars"]
        labels = { "review": "Arvostelu", "stars": "Tähdet" }
        help_texts = { "stars": "Anna tähtiä (0-5)" }
        error_messages = {
            "stars": {
                "max_value": "Anna tähtiä (0-5)",
                "min_value": "Anna tähtiä (0-5)"
            }
        }