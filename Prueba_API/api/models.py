from django.db import models

# Create your models here.
class Payment(models.Model):
    name=models.CharField(max_length=150)
    surname=models.CharField(max_length=50)
    card_number=models.CharField(max_length=50)
    card_cvv=models.IntegerField(null=True)
    total_value=models.BigIntegerField()
    extra_description=models.CharField(max_length=500, blank=True, null=True)
    comission_value=models.FloatField(blank=True, null=True)
