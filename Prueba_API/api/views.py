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
        datos={}
        str_card_number=str(jd['card_number'])
        str_card_cvv=str(jd['card_cvv'])
        float_comission_value=float(jd['total_value'])
        if(len(str_card_number) >= 16 ):
            if(len(str_card_cvv)== 3):
                if(jd['total_value'] >=1000):
                    Payment.objects.create(name=jd['name'], surname=jd['surname'], card_number=jd['card_number'], card_cvv=jd['card_cvv'],total_value=jd['total_value'],extra_description=jd['extra_description'], comission_value=float_comission_value*0.03)
                    datos={'message':'Success'}
                else:
                    datos={'message':'El valor mínimo a pagar es de $1000'}
            else:
                datos={'message':'El código de seguridad de la tarjeta debe contener 3 dígitos'}
        else:
            datos={'message':'El número de tarjeta debe contener al menos 16 dígitos'}
        return JsonResponse(datos)