from bookshelf.models import Book

# Delete the book

book_to_delete = Book.objects.get(id=book.id)
book_to_delete.delete()

# Confirm deletion

Book.objects.all()

# Expected output: <QuerySet []>
