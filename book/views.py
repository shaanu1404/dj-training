from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView

from .models import Book
from .forms import BookForm


class BookListView(ListView):
    template_name = 'books/list.html'
    model = Book
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        q = self.request.GET.get('q', None)
        if q is not None:
            books = Book.objects.filter(title__icontains=q)
            context['book_list'] = books
            context['object_list'] = books

        return context


class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    model = Book
    pk_url_kwarg = 'id'


class BookCreateView(CreateView):
    template_name = 'books/create.html'
    model = Book
    form_class = BookForm
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/edit.html'
    form_class = BookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_url = '/'
