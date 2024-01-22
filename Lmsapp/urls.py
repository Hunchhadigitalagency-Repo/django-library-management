
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', dashboard),
    path('login/', custom_login),
    path('dashboard/', dashboard),

    # category routes
    path('dashboard/category/', category),
    path('dashboard/category/delete/<int:id>', deleteCategory),
    path('dashboard/category/edit/<int:id>', editCategory),

    # book routes
    path('dashboard/books/', books),
    path('dashboard/books/delete/<int:id>', deleteBooks),
    path('dashboard/books/edit/<int:id>', editBooks),

    # student routes
    path('dashboard/students/', student),
    path('dashboard/students/delete/<int:id>', deleteStudent),
    path('dashboard/students/edit/<int:id>', editStudent),


    # borrow routes
    path('dashboard/borrow/', borrow),
    path('dashboard/borrow/delete/<int:id>', deleteBorrow),
    path('dashboard/borrow/edit/<int:id>', editBorrow),

]
