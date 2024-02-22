from django.db import models
# NAME
# Author
# Publisher
# Date of Publication
# Genre
# No of Pages
# Book Location
# Create your models here.
class BookDetails(models.Model):
    Book_name=models.CharField(max_length=300)
    Author=models.CharField(max_length=300)
    Publisher=models.CharField(max_length=300)
    Publication_date = models.DateField()
    Genre=models.CharField(max_length=200)
    Pages = models.IntegerField()
    Location=models.TextField(max_length=300)

    def __str__(self):
        return self.Book_name


    