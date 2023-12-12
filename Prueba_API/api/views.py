from typing import Any
from django.utils.decorators import method_decorator
from django import http
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
import json

# Create your views here.

class PaymentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        Payment.objects.create(name=jd['name'], surname=jd['surname'], card_number=jd['card_number'], card_cvv=jd['card_cvv'],total_value=jd['total_value'],extra_description=jd['extra_description'])
        datos={'message':'Success'}
        return JsonResponse(datos)