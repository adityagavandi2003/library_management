from django.shortcuts import render,get_object_or_404
from book.models import Book
# Create your views here.
def home(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'home.html',context)

def book(request,pk):
    book = get_object_or_404(Book,id=pk)
    context = {
        'book':book
    }
    return render(request,'book.html',context)