from django.db import models


class Category(models.Model):
    name = models.CharField( max_length=500)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length = 1000)
    author_name = models.CharField(max_length = 1000)
    no_of_copies = models.IntegerField()
    category_id =  models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length = 1000)
    phone_number = models.CharField(max_length=15)
    image = models.FileField(upload_to='students/')
    student_id = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class BookBorrow(models.Model):
    student_id = models.ForeignKey("Student", on_delete=models.CASCADE)
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE)
    borrowed_at = models.DateField()
    returned_at = models.DateField(blank = True, null = True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.name} borrowed {self.book_id.name}"





