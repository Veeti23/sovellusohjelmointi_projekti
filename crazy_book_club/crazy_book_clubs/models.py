from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
#Book
class Book(models.Model):
    #Name the book
    name = models.CharField(max_length=400)

    #Add book author in Json list
    authors = models.JSONField()

    #Add book published year
    year_published = models.IntegerField()

    #Automatically set the date when the book is first added
    date_added = models.DateTimeField(
        auto_now_add=True
        )
    #Automatically update the timestamp whenever the book is modified
    date_modifield = models.DateTimeField(
        auto_now=True
        )

    def __str__(self):

        authors_list = ', '.join(self.authors)
        return f"{self.name} by {authors_list}, Published in {self.year_published}"


#Review
class Review(models.Model):
    #ForeignKey to link each specific book
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE,
        related_name="reviews",
        help_text="The book being reviewed"
        )

    #Field to store the name of the reviewer
    reviewer_name = models.CharField(
        max_length=100,
        help_text="Name of the person reviewing the book"
        )

    #The review text
    my_review = models.TextField()

    #Stars rating for the review
    stars = models.IntegerField(
        # min rating number is 0
        # max rating number is 5
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
            ],
            help_text="Rating of the book (0-5)"
        )

    #Indicate if the review is unfinished
    unfinished = models.BooleanField(
        default=False
        )
    #Automatically set the date when the review is first added
    date_added = models.DateTimeField(
        auto_now_add=True
        )
    #Automatically update the timestamp whenever the review is modified
    date_modified = models.DateTimeField(
        auto_now=True
        )

    #Meta class to specify options for the Review model.
    """
    class Meta:
        ordering = ['-date_added']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'reviewer_name'],
                name='unique_book_reviewer'
            )
        ]
    """
    def __str__(self):
        
        status = "Unfinished" if self.unfinished else "Complete"
        return f"Review by {self.reviewer_name} for {self.book.name}: {self.stars}/5 Stars ({status})"
