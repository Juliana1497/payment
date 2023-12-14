from typing import Any
from django.utils.decorators import method_decorator
from django import http
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
import json
import re

# Create your views here.

class PaymentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        datos={}
        #str_card_number=str(jd['card_number'])
        str_card_cvv=str(jd['card_cvv'])
        float_comission_value=float(jd['total_value'])
        if(len(jd['card_number']) >= 16 ):
            final_card_number=hide_card_number(jd['card_number'])
            if(len(str_card_cvv)== 3):
                if(jd['total_value'] >=1000):
                    Payment.objects.create(name=jd['name'], surname=jd['surname'], card_number=final_card_number, total_value=jd['total_value'],extra_description=jd['extra_description'], comission_value=float_comission_value*0.03+((float_comission_value*0.03)*0.19)+(float_comission_value*0.015))
                    datos=card_type(jd['card_number'])  
                else:
                    datos={'message':'El valor mínimo a pagar es de $1000'}
            else:
                datos={'message':'El código de seguridad de la tarjeta debe contener 3 dígitos'}
        else:
            datos={'message':'El número de tarjeta debe contener al menos 16 dígitos'}
        return JsonResponse(datos)
    

def hide_card_number(chain):
    # Utilizar una expresión regular para encontrar números de cualquier longitud
    pattern = r'(\d*)(\d{4})'
    
    def replace(match):
        # Reemplazar los dígitos anteriores a los últimos 4 con asteriscos y mantener los últimos 4 dígitos
        return '*' * len(match.group(1)) + match.group(2)
    
    # Aplicar la expresión regular y la función de reemplazo a la cadena
    resultado = re.sub(pattern, replace, chain)
    
    return resultado

def card_type(chain):
    first_number=int(chain[0])
    if first_number== 4:
        datos = {'message':'El tipo de tarjeta es Visa'}
    elif first_number == 5:
        datos = {'message':'El tipo de tarjeta es Mastercard'}
    elif first_number == 3:
        datos = {'message':'El tipo de tarjeta es Diners'}
    else:
        datos = {'message':'El tipo de tarjeta es diferente a Visa, Mastercard o Diners'}
    return datos