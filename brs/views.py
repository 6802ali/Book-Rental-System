from .models import *
from .serializers import * 
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# class OccupationViewSet(viewsets.ModelViewSet):
#     queryset = Occupation.objects.all()
#     serializer_class = OccupationSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
    
#     def get_serializer_class(self):
#         if self.action == 'list' or self.action == 'retrieve':
#             return BookGetSerializer
#         return BookSerializer

# class OfferViewSet(viewsets.ModelViewSet):
#     queryset = Offer.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list' or self.action == 'retrieve':
#             return OfferGetSerializer
#         return OfferSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list' or self.action == 'retrieve':
#             return UserGetSerializer
#         return UserSerializer

# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class LibrarianViewSet(viewsets.ModelViewSet):
#     queryset = Librarian.objects.all()
#     serializer_class = LibrarianSerializer

