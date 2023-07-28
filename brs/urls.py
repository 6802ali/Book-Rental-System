from rest_framework import routers
from django.urls import include, path, re_path
from .views import *
from . import views 
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'books', BookViewSet)
router.register(r'offer', OfferViewSet)
router.register(r'role', RoleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]   
