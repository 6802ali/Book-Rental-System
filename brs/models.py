from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)

class Role(models.Model):
    Role_name = models.CharField(max_length=20)

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_method = models.CharField(max_length=50)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class Book(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_type = models.CharField(max_length=50)
    
class Offer(models.Model):
    offer_id = models.IntegerField(primary_key=True) 
    # offer_percentage = models.IntegerField(default=0) # when i add this attribute and migrate "no such column: brs_offer.offer_percentage,"
    book = models.OneToOneField(Book, on_delete=models.CASCADE)      
    
