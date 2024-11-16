# relationship_app/views.py
from django.shortcuts import render
from .models import Book  # Assuming you have a Book model
from django.views.generic import DetailView
from .models import Library
from django.views.generic.detail import DetailView



def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template to use
    context_object_name = 'library'  # This is the name to use in the template for the object