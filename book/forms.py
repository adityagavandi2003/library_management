from django import forms
from book.models import Book,Category,Author

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','category','price','image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter book title'}),
            'author': forms.Select(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter author name'}),
            'category': forms.Select(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter book category'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter book price'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'select image'}),
        }

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter author name'}),
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter author name'}),
        }