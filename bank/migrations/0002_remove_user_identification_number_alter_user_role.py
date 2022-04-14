# Generated by Django 4.0.3 on 2022-04-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='identification_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Client', 'Client'), ('Operator', 'Operator'), ('Manager', 'Manager'), ('Company-specialist', 'CompanySpecialist'), ('Administrator', 'Administrator')], default=('Client', 'Client'), max_length=200),
        ),
    ]
