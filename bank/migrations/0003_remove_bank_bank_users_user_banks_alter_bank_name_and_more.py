# Generated by Django 4.0.3 on 2022-04-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_remove_user_identification_number_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='bank_users',
        ),
        migrations.AddField(
            model_name='user',
            name='banks',
            field=models.ManyToManyField(to='bank.bank'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Client', 'Client'), ('Operator', 'Operator'), ('Manager', 'Manager'), ('Company-specialist', 'CompanySpecialist'), ('Administrator', 'Administrator')], default='Client', max_length=200),
        ),
    ]
