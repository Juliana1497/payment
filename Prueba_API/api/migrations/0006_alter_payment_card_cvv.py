# Generated by Django 4.1.13 on 2023-12-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_payment_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_cvv',
            field=models.IntegerField(null=True),
        ),
    ]