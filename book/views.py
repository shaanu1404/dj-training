from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    template_name = 'books/list.html'
    model = Book
    queryset = Book.objects.all()