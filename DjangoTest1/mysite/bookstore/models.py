from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField(max_length=4)

    def __str__(self):
        return self.title+self.price


class BookList(models.Model):
    book = models.ForeignKey(Book)

