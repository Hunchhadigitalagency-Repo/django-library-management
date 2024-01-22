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
    if request.method == "POST":
        req_name = request.POST.get('name')
        req_student_id = request.POST.get('student_id')
        req_image = request.FILES.get('image')
        req_phone_number = request.POST.get('phone_number')

        student = Student.objects.create(
            name=req_name,
            student_id = req_student_id,
            image = req_image,
            phone_number = req_phone_number
            )
        if student:
            return redirect('/dashboard/students')
        else:
            return render(request,'/dashboard/student',{'error':'Error Something went wrong '})
    else:    
        if request.user.is_authenticated:
            students = Student.objects.all()
            return render(request, 'dashboard/student/index.html',{'students':students})
        else:
            return redirect('/login/')
        
def deleteStudent(request,id):
    if request.user.is_authenticated:
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('/dashboard/students/')
    else:
        return redirect('/login')
    
def editStudent(request,id):
    if request.method == "POST":
        req_name = request.POST.get('name')
        req_student_id = request.POST.get('student_id')
        req_image = request.FILES.get('image')
        req_phone_number = request.POST.get('phone_number')

        student = Student.objects.get(id=id)

        student.name=req_name
        student.student_id = req_student_id
        student.image = req_image
        student.phone_number = req_phone_number
        student.save()

        if student:
            return redirect('/dashboard/students')
        else:
            return render(request,'/dashboard/student/index.html',{'error':'Error Something went wrong '})
    else:    
        if request.user.is_authenticated:
            student = Student.objects.get(id=id)
            return render(request, 'dashboard/student/edit.html',{'student':student})
        else:
            return redirect('/login/')

def borrow(request):
    if request.method == "POST":
        req_book_id = request.POST.get('book_id')
        req_student_id = request.POST.get('student_id')
        req_borrowed_at = request.POST.get('borrowed_at')

        book = Book.objects.get(id=req_book_id)
        book.no_of_copies -= 1
        book.save()
        student = Student.objects.get(id=req_student_id)

        borrow = BookBorrow.objects.create(
        book_id=book,
        student_id = student,
        borrowed_at = req_borrowed_at,
        )

        borrow.save();

        if borrow:
            return redirect('/dashboard/borrow/')
        else:
            return render(request,'/dashboard/borrow/index.html',{'error':'Error Something went wrong '})
    else:    
        if request.user.is_authenticated:
            students = Student.objects.all();
            books = Book.objects.all();
            borrows = BookBorrow.objects.all();
            return render(request, 'dashboard/borrow/index.html',{'students':students,'books':books,'borrows':borrows})
        else:
            return redirect('/login/')
        
def deleteBorrow(request,id):
    if request.user.is_authenticated:
        borrow = BookBorrow.objects.get(id=id)
        borrow.delete()
        return redirect('/dashboard/borrow/')
    else:
        return redirect('/login')
    
def editBorrow(request,id):
    if request.method == "POST":
        req_book_id = request.POST.get('book_id')
        req_student_id = request.POST.get('student_id')
        req_borrowed_at = request.POST.get('borrowed_at')
        req_returned_at = request.POST.get('returned_at')

        if req_returned_at:
            is_returned_value = True

        book = Book.objects.get(id=req_book_id)
        student = Student.objects.get(id=req_student_id)

        if req_returned_at:
            is_returned_value = True
            book.no_of_copies += 1
            book.save()


        borrow = BookBorrow.objects.get(id=id)
        borrow.book_id=book
        borrow.student_id = student
        if req_returned_at:
            borrow.returned_at = req_returned_at
            borrow.is_returned = is_returned_value

        borrow.save();

        if borrow:
            return redirect('/dashboard/borrow')
        else:
            return render(request,'/dashboard/borrow/index.html',{'error':'Error Something went wrong '})
    else:    
        if request.user.is_authenticated:
            borrow = BookBorrow.objects.get(id=id)
            students = Student.objects.all();
            books = Book.objects.all();
            return render(request, 'dashboard/borrow/edit.html',{'students':students,'books':books,'borrow':borrow})
        else:
            return redirect('/login/')