from bookshelf.models import Book

# Retrieve the book you created

retrieved_book = Book.objects.get(id=book.id)

# Expected output: shows title='1984', author='George Orwell', publication_year=1949

retrieved_book.title, retrieved_book.author, retrieved_book.publication_year
