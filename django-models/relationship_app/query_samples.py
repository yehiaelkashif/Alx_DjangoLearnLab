# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")

# Query 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Many-to-Many relation
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # One-to-One relation
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'")

# Example usage:
# books_by_author('J.K. Rowling')
# books_in_library('City Library')
# librarian_for_library('City Library')
