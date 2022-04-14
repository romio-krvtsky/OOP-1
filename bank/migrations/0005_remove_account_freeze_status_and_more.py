# Generated by Django 4.0.3 on 2022-04-14 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_credit_credit_status_installment_installment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='freeze_status',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='freeze_status',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='freeze_status',
        ),
        migrations.RemoveField(
            model_name='installment',
            name='freeze_status',
        ),
        migrations.AddField(
            model_name='user',
            name='freeze_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='credit',
            name='payment_day',
            field=models.DateField(default=datetime.date(2022, 4, 14)),
        ),
        migrations.AlterField(
            model_name='installment',
            name='payment_day',
            field=models.DateField(default=datetime.date(2022, 4, 14)),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.CharField(default='', max_length=20, verbose_name='passport number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Client', 'Client'), ('Operator', 'Operator'), ('Manager', 'Manager'), ('Company-specialist', 'CompanySpecialist'), ('Administrator', 'Administrator')], default='Client', max_length=30),
        ),
    ]
