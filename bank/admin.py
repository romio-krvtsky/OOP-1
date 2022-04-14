from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'passport_number', 'role',)
    list_display_links = ('username', )


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sum', 'bank', 'opening_date')
    list_display_links = ('user', 'bank')


class DepositAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sum', 'percentage_rate', 'bank', 'opening_date',)
    list_display_links = ('sum', 'bank',)


class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sum', 'percentage_rate', 'bank', 'opening_date', 'months', 'credit_status')
    list_display_links = ('sum', 'bank', 'credit_status')


class InstallmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sum', 'bank', 'company', 'opening_date', 'months', 'installment_status')
    list_display_links = ('sum', 'bank', 'installment_status')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('legal_name', 'company_type', 'BIC', 'legal_address')
    list_display_links = ('legal_name',)


class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank_email')
    list_display_links = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(Installment, InstallmentAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Economics)
