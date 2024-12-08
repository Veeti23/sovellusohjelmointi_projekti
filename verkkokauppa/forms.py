from django import forms
from .models import Review

# Create a form for the Review model
# The form will have fields for the review and stars
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