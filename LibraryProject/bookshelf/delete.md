

from bookshelf.models import Book

# Delete the Book instance
book.delete()

# Try to retrieve all books to confirm deletion
Book.objects.all()

