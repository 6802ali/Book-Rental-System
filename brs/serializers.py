from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class BookGetSerializer(serializers.ModelSerializer):
    Author = AuthorSerializer()
    
    class Meta:
        model = Book
        fields = '__all__'        

class BookSerializer(serializers.ModelSerializer):
    Author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

class OfferGetSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Offer
        fields = '__all__'
        
class OfferSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Offer
        fields = '__all__'

class UserGetSerializer(serializers.ModelSerializer):
    role= RoleSerializer()

    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['password'] = user.password
        # ...

        return token