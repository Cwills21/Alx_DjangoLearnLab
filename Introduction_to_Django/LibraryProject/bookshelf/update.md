from bookshelf.models import Book

# Retrieve the book again

book_to_update = Book.objects.get(id=book.id)

# Update the title

book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Expected output: updated title

book_to_update.title
