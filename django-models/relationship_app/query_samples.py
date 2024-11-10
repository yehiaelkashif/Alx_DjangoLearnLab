# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(book.title)

# Query 2: List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Many-to-Many relation
    for book in books:
        print(book.title)

# Query 3: Retrieve the librarian fo
