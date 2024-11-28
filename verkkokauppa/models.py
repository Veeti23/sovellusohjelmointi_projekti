from django.db import models

# Create your models here.
class Tuotteet(models.Model):
    nimi = models.CharField(max_length=100)
    hinta = models.DecimalField(max_digits=5, decimal_places=2)
    kuvaus = models.TextField()

    def ___str__(self):
        # Palauttaa tuotteen nimen ja hinnan
        return self.nimi, self.hinta 