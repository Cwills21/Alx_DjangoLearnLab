```python
from bookshelf.models import Book
book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: updated title "Nineteen Eighty-Four"
```
