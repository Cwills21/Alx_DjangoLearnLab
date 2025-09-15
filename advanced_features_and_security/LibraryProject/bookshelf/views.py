# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    # Safe ORM query, no raw SQL
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_search(request):
    query = request.GET.get('q', '')
    # Safe filter, no injection risk
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # validates and cleans data
            form.save()
            # redirect or render success
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
