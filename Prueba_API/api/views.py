from typing import Any
from django.utils.decorators import method_decorator
from django import http
from django.http.response import JsonResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
import json
import re

class PaymentView(View):

    #It will only be executed if it is authenticated
    permission_classes = [IsAuthenticated]

    #skip the restriction CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        datos={}
        str_card_cvv=str(jd['card_cvv'])
        float_comission_value=float(jd['total_value'])

        if(len(jd['card_number']) >= 16 ):
            final_card_number=hide_card_number(jd['card_number'])
            if(len(str_card_cvv)== 3):
                if(jd['total_value'] >=1000):
                    Payment.objects.create(name=jd['name'], surname=jd['surname'], card_number=final_card_number, total_value=jd['total_value'],extra_description=jd['extra_description'], comission_value=float_comission_value*0.03+((float_comission_value*0.03)*0.19)+(float_comission_value*0.015))
                    datos=card_type(jd['card_number'])  
                else:
                    datos={'message':'Error. El valor mínimo a pagar es de $1000'}
            else:
                datos={'message':'Error. El código de seguridad de la tarjeta debe contener 3 dígitos'}
        else:
            datos={'message':'Error. El número de tarjeta debe contener al menos 16 dígitos'}

        return JsonResponse(datos)
    
# Replace the digits before the last 4 with asterisks and keep the last 4 digits
def hide_card_number(chain):
    # Regular expression to find numbers of any length
    pattern = r'(\d*)(\d{4})'
    
    def replace(match):
        # Replace the digits before the last 4 with asterisks and keep the last 4 digits
        return '*' * len(match.group(1)) + match.group(2)
    
    # Apply regular expression and replace function to string
    result = re.sub(pattern, replace, chain)
    
    return result

# With the first card number entered, the type of card is inferred
def card_type(chain):
    first_number=int(chain[0])
    if first_number== 4:
        datos = {'message':'Guardado. El tipo de tarjeta es Visa'}
    elif first_number == 5:
        datos = {'message':'Guardado. El tipo de tarjeta es Mastercard'}
    elif first_number == 3:
        datos = {'message':'Guardado. El tipo de tarjeta es Diners'}
    else:
        datos = {'message':'Guardado. El tipo de tarjeta es diferente a Visa, Mastercard o Diners'}
    return datos