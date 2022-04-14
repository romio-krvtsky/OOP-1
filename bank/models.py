from datetime import date

from django.contrib.auth.models import User, AbstractUser

from django.db import models


class Economics(models.Model):
    class Meta:
        verbose_name_plural = 'economics'

    freeze_status = models.BooleanField(default=False)

    def __str__(self):
        if self.freeze_status:
            return f'freezing is true'
        return f'no freezing'


###########################################################################################
class User(AbstractUser):
    phone = models.CharField(max_length=13, default='', verbose_name='phone')
    passport_number = models.CharField(max_length=20, default='', verbose_name='passport number')
    roles = (
        ('Client', 'Client'),
        ('Operator', 'Operator'),
        ('Manager', 'Manager'),
        ('Company-specialist', 'CompanySpecialist'),
        ('Administrator', 'Administrator'),
    )
    role = models.CharField(max_length=30, choices=roles, default=roles[0][1])

    banks = models.ManyToManyField('Bank')

    def __str__(self):
        return f"{self.username} ({self.role})"


#############################################################################################################

class FinancialEntity(models.Model):
    class Meta:
        abstract = True

    sum = models.PositiveBigIntegerField(default=0)
    opening_date = models.DateField(auto_now_add=date.today())
    block_status = models.BooleanField(default=False)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)


class Account(FinancialEntity):
    """Лицевой счет в банке"""

    def __str__(self):
        return f"Account {self.user_id} of {self.user.username}, total: {self.sum} BYN"


class Deposit(FinancialEntity):
    """Вклад в банке"""
    months = models.PositiveSmallIntegerField(default=0)
    percentage_rate = models.FloatField(default=1.0)

    def __str__(self):
        return f"Deposit of {self.user.username}, {self.sum} , {self.opening_date}"


class Credit(FinancialEntity):
    months = (3, 3), (6, 6), (9, 9), (12, 12), (24, 24), (48, 48)
    payment_day = models.DateField(default=date.today())
    percentage_rate = models.FloatField(default=0.0)
    months = models.PositiveSmallIntegerField(default=months[0][0], choices=months)
    states = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accepted', 'accepted')
    )
    credit_status = models.CharField(max_length=200, choices=states, default=states[1][0])

    def __str__(self):
        return f"Credit of {self.user.username}, {self.sum} BYN for {self.months}"


class Installment(FinancialEntity):
    """Рассрочка в банке для др. предприятия"""
    payment_day = models.DateField(default=date.today())
    months = models.PositiveSmallIntegerField(default=1)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    states = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accepted', 'accepted')
    )
    installment_status = models.CharField(max_length=200, choices=states, default=states[1][0])

    def __str__(self):
        return f"Installment of {self.user.username} - {self.sum} BYN"


#############################################################################################################

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'

    company_type = models.CharField(max_length=200, default='')
    legal_name = models.CharField(max_length=200, default='')
    BIC = models.CharField(max_length=200, default='')
    legal_address = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"{self.company_type} {self.legal_name}"


#############################################################################################################


class Bank(models.Model):
    name = models.CharField(max_length=200, default='', unique=True)
    bank_email = models.CharField(max_length=200, default='')

    # bank_users = models.ManyToManyField(User)
    # companies = models.ForeignKey('Company', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Bank <<{self.name}>>"
