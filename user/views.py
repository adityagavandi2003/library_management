from django.shortcuts import render,redirect,get_object_or_404
from book.models import Book,Category,Author
from user.models import Order
from django.contrib.auth.models import User
from book.forms import AddBookForm,AddAuthorForm,AddCategoryForm
from user.forms import RegistrationForm,LoginForm
from user.emailauthentication import EmailBackend
from django.contrib.auth import authenticate, login as auth_login,logout

# Create your views here.
def dashboard(request):
    total_books = Book.objects.all()
    books = Book.objects.all().order_by('-id')[:10]
    total_order = Order.objects.all()
    users = User.objects.all()
    context = {
        'books':books,
        'users':users,
        'total_order':total_order,
        'total_books':total_books,
    }
    return render(request,'dashboard.html',context)

def users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'users.html',context)

def addbooks(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddBookForm()
    context = {
        'form':form,
    }
    return render(request,'addbooks.html',context)

def books(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'managebook.html',context)

def updatebook(request,pk):
    book = get_object_or_404(Book,id=pk)
    if request.method == 'POST':
        form = AddBookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddBookForm(instance=book)
    context = {
        'book':book,
        'form':form,
    }
    return render(request,'addbooks.html',context)

def deletebook(request,pk):
    book = get_object_or_404(Book,id=pk)
    book.delete()
    return redirect('dashboard')

def updateuser(request,pk):
    user = get_object_or_404(User,id=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            return redirect('dashboard')
    else:
        form = RegistrationForm(instance=user)
    context = {
        'user':user,
        'form':form,
    }
    return render(request,'register/signup.html',context)

def deleteuser(request,pk):
    user = get_object_or_404(user,id=pk)
    user.delete()
    return redirect('dashboard')

def updateauthor(request,pk):
    author_name = get_object_or_404(Author,id=pk)
    if request.method == 'POST':
        form = AddAuthorForm(request.POST,instance=author_name)
        if form.is_valid():
            form.save()
            return redirect('author')
    else:
        form = AddAuthorForm(instance=author_name)
    context = {
        'author':author,
        'form':form,
    }
    return render(request,'addauthor.html',context)

def deleteauthor(request,pk):
    author_name = get_object_or_404(Author,id=pk)
    author_name.delete()
    return redirect('author')

def updatecategory(request,pk):
    category_name = get_object_or_404(Category,id=pk)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST,instance=category_name)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = AddCategoryForm(instance=category_name)
    context = {
        'category':category_name,
        'form':form,
    }
    return render(request,'addcategory.html',context)

def deletecategory(request,pk):
    category_name = get_object_or_404(Category,id=pk)
    category_name.delete()
    return redirect('category')

def author(request):
    form = AddAuthorForm()
    author_list = Author.objects.all()
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddAuthorForm()
    context = {
        'form':form,
        'author_list':author_list,
    }
    return render(request,'addauthor.html',context)

def category(request):
    form = AddCategoryForm()
    category_list = Category.objects.all()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddCategoryForm()
    context = {
        'form':form,
        'category_list':category_list,
    }
    return render(request,'addcategory.html',context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password = form.cleaned_data['password']
            backend = EmailBackend()
            user = backend.authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect('dashboard')
                else:
                    return redirect("home")  # Redirect to home or dashboard
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()
    context = {
        'form':form,
    }
    return render(request,'register/login.html',context)

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            auth_login(request, user)  
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request,'register/signup.html',context)

def user_logout(request):
    logout(request)
    return redirect('login')


def order(request,pk):
    book = get_object_or_404(Book,id=pk)
    user = request.user
    ordered = Order.objects.filter(book=book, user=user).first()

    if not ordered:
        new_ordered = Order.objects.create(book=book, user=user)
        return redirect('home')
    
    return render(request,'order.html')