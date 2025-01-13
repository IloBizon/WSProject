from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.PROTECT)
