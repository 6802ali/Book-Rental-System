from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=50)

# class Role(models.Model):
#     role_id = models.IntegerField(default=0)
#     role_title = models.CharField(max_length=15)

# class User(models.Model):
#     user_id = models.IntegerField(primary_key=True)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=100)

# class Book(models.Model):
#     Author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     book_id = models.IntegerField()
#     book_name = models.CharField(max_length=100)
#     book_type = models.CharField(max_length=50)
    
# class Offer(models.Model):
#     offer_id = models.IntegerField()
#     book = models.OneToOneField(Book, on_delete=models.CASCADE)      
    
# class Payment(models.Model):
#     payment_id = models.IntegerField(default=0)
#     payment_method = models.CharField(max_length=10)

# class Order(models.Model):
#     order_id = models.IntegerField()
#     books = models.ManyToManyField('Book')
#     payment = models.OneToOneField(Payment, on_delete=models.CASCADE)

# class Cart(models.Model):
#     delivery_location = models.CharField(max_length=50)
#     delivery_date = models.DateField()
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)

# ka logic elmafroud byb2a feh obj men Order mawgod fel Cart, bas 
# elclass diagram elrelation mabenhom 1 to many fa lama get a3melha ka syntex tl3a berror
# elmwdo3 8areb ?

# a7ot object men eloofer fel librarian wala el3aks ?