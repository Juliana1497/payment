# Generated by Django 4.1.13 on 2023-12-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_payment_comission_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=50),
        ),
    ]
