from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    city = models.CharField(max_length=200)
    num_of_books = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publish = models.CharField(max_length=200)
    isbn = models.CharField(max_length=100)
    book_num = models.CharField(max_length=100)
    publish_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name
