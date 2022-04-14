
from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('registration/', registration_page, name='registration'),
    path('logout/', logout_user, name='logout'),
    path('client/', client_page, name='client_page'),
    path('manager/', manager_page, name='manager_page'),
    path('management/', financial_management, name='financial_management'),
    path('my_profile/', client_info, name='client_info'),
    path('money_transaction/', money_transaction, name='money_transaction'),
    path('account/', open_account, name='open_account'),
    path('deposit/', open_deposit, name='open_deposit'),
    path('credit/', apply_for_credit, name='apply_for_credit'),
    path('installment/', apply_for_installment, name='apply_for_installment'),

]
