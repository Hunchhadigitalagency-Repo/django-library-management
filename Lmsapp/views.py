from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.

def index(request):
    return render(request,'auth/login.html')

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request,'auth/login.html')
    else:
        if request.user.is_authenticated == True:
            return redirect('/dashboard/')
        else:    
            return render(request,'auth/login.html')
    
def dashboard(request):
    if request.user.is_authenticated == True:
        books = Book.objects.all()
        return render(request, 'dashboard/index.html',{'books':books})
    else:
        return redirect('/login/')


def category(request):
    if request.method == "POST":
        req_name = request.POST.get('name')
        category = Category.objects.create(name=req_name)
        if category:
            return redirect('/dashboard/category')
    else:
        if request.user.is_authenticated:
            categories = Category.objects.all()
            return render(request, 'dashboard/category/index.html', {'categories': categories})
        else:
            return redirect('/login/')
        

def editCategory(request, id):
    if request.method == "POST":
        req_name = request.POST.get('name')
        category = Category.objects.get(id=id)
        category.name = req_name
        category.save()
        if category:
            return redirect('/dashboard/category')
    else:    
        if request.user.is_authenticated:
            category = Category.objects.get(id=id)
            return render(request,'dashboard/category/edit.html',{'category':category})
        else:
            return redirect('/login/')
    
def deleteCategory(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('/dashboard/category/')
    else:
        return redirect('/login/')

def books(request):
    if request.method == "POST":
        req_name = request.POST.get('name')
        req_author_name = request.POST.get('author_name')
        req_no_of_copies = request.POST.get('no_of_copies')
        req_category_id = request.POST.get('category_id')
        category = Category.objects.get(id = req_category_id)

        book = Book.objects.create(
            name=req_name,
            author_name = req_author_name,
            no_of_copies = req_no_of_copies,
            category_id = category
            )
        if book:
            return redirect('/dashboard/books')
    else:    
        if request.user.is_authenticated:
            books = Book.objects.all()
            categories = Category.objects.all()
            return render(request, 'dashboard/books/index.html', {'books': books,'categories':categories})
        else:
            return redirect('/login/')
        
def deleteBooks(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/dashboard/books/')
    else:
        return redirect('/login')

def editBooks(request,id):
    if request.method == "POST":
        req_name = request.POST.get('name')
        req_author_name = request.POST.get('author_name')
        req_no_of_copies = request.POST.get('no_of_copies')
        req_category_id = request.POST.get('category_id')
        category = Category.objects.get(id = req_category_id)
       
        book = Book.objects.get(id=id)
        book.name = req_name
        book.author_name = req_author_name
        book.no_of_copies = req_no_of_copies
        book.category_id = category
        book.save()

        if book:
            return redirect('/dashboard/books')
    else:    
        if request.user.is_authenticated:
            categories = Category.objects.all()
            book = Book.objects.get(id=id)

            return render(request,'dashboard/books/edit.html',{'categories':categories,'book':book})
        else:
            return redirect('/login/')


def student(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/student/index.html')
    else:
        return redirect('/login/')

def borrow(requset):
    if requset.user.is_authenticated:
        return render(requset, 'dashboard/borrow/index.html')
    else:
        return redirect('/login/')