book=Book(title="1984",author="George Orwell",publication_year=1949)
book.save()

my_book = Book.objects.get(id=book.id)
print(my_book.title, my_book.author, my_book.publication_year)
1984 George Orwell 1949

my_book.title="Nineteen Eighty-Four"
my_book.delete()
(1, {'bookshelf.Book': 1})
(1, {'bookshelf.Book': 1})
(1, {'bookshelf.Book': 1})
print(Book.objects.all())
<QuerySet []>
