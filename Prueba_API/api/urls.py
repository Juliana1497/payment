from django.urls import path
from .views import PaymentView
from rest_framework_simplejwt import views as jwt_views

urlpatterns=[
    #URLs to authenticate
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #URL to API REST
    path('payment-tc/process', PaymentView.as_view(), name='payment_list'),
]