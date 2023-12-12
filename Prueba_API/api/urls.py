from django.urls import path
from .views import PaymentView

urlpatterns=[
    path('payment-tc/process', PaymentView.as_view(), name='payment_list')
]