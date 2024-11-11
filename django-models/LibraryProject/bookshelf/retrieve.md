# Retrieve the Book instance
book = Book.objects.get(title="1984")

# Display the details of the book
book.title, book.author, book.publication_year
