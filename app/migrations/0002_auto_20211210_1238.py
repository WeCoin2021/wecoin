# Generated by Django 3.2.8 on 2021-12-10 09:08

from decimal import Decimal
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction_history',
            name='buyMoney_perone',
        ),
        migrations.RemoveField(
            model_name='transaction_history',
            name='sellMoney_perone',
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='Money_perone',
            field=models.DecimalField(decimal_places=5, default=Decimal('0.0000'), max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='type',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='transaction_history',
            name='quantity',
            field=models.DecimalField(decimal_places=5, default=Decimal('0.0000'), max_digits=14, null=True),
        ),
    ]
