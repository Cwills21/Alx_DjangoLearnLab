# bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # do something with form.cleaned_data
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
