from django.shortcuts import render
from .models import *
from django.views.generic import ListView

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'


