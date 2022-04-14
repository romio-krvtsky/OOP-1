from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'passport_number']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TransactionForm(forms.Form):
    beneficiary_account = forms.ModelChoiceField(Account.objects)
    sum = forms.IntegerField(min_value=1)


class ManagementForm(forms.Form):
    account = forms.ModelChoiceField(Account.objects, required=False)
    account_block_status = forms.BooleanField(required=False)
    deposit = forms.ModelChoiceField(Deposit.objects, required=False)
    deposit_block_status = forms.BooleanField(required=False)
    credit = forms.ModelChoiceField(Credit.objects, required=False)
    states = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accepted', 'accepted')
    )
    credit_status = forms.ChoiceField(choices=states, required=False)
    installment = forms.ModelChoiceField(Installment.objects, required=False)
    installment_status = forms.ChoiceField(choices=states, required=False)


class OpenAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank']


class OpenDepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['sum', 'bank', 'months', 'percentage_rate']


class ApplyForCreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['sum', 'bank', 'months', 'percentage_rate']


class ApplyForInstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = ['sum', 'company', 'bank', 'months']
