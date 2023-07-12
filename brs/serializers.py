from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# class BookGetSerializer(serializers.ModelSerializer):
#     Author = AuthorSerializer()
    
#     class Meta:
#         model = Book
#         fields = '__all__'        

# class BookSerializer(serializers.ModelSerializer):
#     Author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

#     class Meta:
#         model = Book
#         fields = '__all__'
        
# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = '__all__'

# class UserGetSerializer(serializers.ModelSerializer):
#     role= RoleSerializer()

#     class Meta:
#         model = User
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

#     class Meta:
#         model = User
#         fields = '__all__'

# class OfferGetSerializer(serializers.ModelSerializer):
#     book = BookSerializer()

#     class Meta:
#         model = Offer
#         fields = '__all__'

# class OfferSerializer(serializers.ModelSerializer):
#     book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

#     class Meta:
#         model = Offer
#         fields = '__all__'

# class LibrarianSerializer(UserSerializer):
#     offers = OfferSerializer(many=True, read_only=True)
#     class Meta:
#         model = Librarian
#         fields = '__all__'

# class PaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     payment = PaymentSerializer(many=True, read_only=True)
#     librarian = LibrarianSerializer(many=True, read_only=True)
#     book = BookSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = '__all__'

# class CustomerSerializer(UserSerializer):
#     payment = PaymentSerializer(many=True, read_only=True)
#     order = OrderSerializer(many=True, read_only=True)
#     class Meta:
#         model = Customer
#         fields = '__all__'
    
# class CartSerializer(serializers.ModelSerializer):
#     order = OrderSerializer(many=True, read_only=True)
#     class Meta:
#         model = Cart
#         fields = '__all__'

