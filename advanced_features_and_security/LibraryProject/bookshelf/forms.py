# bookshelf/forms.py
from django import forms
from .models import Book  # import your model if needed

# Existing BookForm (if you already have it)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']


# 👇 This is the new ExampleForm they’re asking for
class ExampleForm(forms.Form):
    """
    Example form to demonstrate CSRF and input validation.
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'}),
        required=True,
        label="Message"
    )
