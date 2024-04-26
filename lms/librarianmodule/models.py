from django.db import models

# Create your models here.
class BookDetails(models.Model):
    Book_name=models.CharField(max_length=300)
    Author=models.CharField(max_length=300)
    Publisher=models.CharField(max_length=300)
    Publication_date = models.DateField()
    Genre=models.CharField(max_length=200)
    Pages = models.IntegerField()
    Location=models.TextField(max_length=300)
    Picture = models.ImageField(upload_to="books/images",default="")

    def __str__(self):
        return self.Book_name

# models.py

from django.db import models
class Order(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    adress = models.CharField(max_length=100, default="Unknown") # Field for customer name
    book = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    # Optionally, you can add more fields to store additional information about the order
    # For example, order date, etc.

    def __str__(self):
        return f"Order: {self.name} - Book: {self.book} - Quantity: {self.quantity} - adress: {self.adress}"





    