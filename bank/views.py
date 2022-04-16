from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def registration_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'bank/registration.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.role == 'Client':
                        return redirect('client_page')
                    if request.user.role == 'Operator':
                        return redirect('operator_page')
                    if request.user.role == 'Manager':
                        return redirect('manager_page')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'bank/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def client_page(request):
    context = {
        'freezing': freezing
    }
    return render(request, 'bank/client_page.html', context)


@login_required(login_url='login')
def manager_page(request):
    accounts = Account.objects.all()
    deposits = Deposit.objects.all()
    credits = Credit.objects.all()
    installments = Installment.objects.all()
    context = {
        'deposits': deposits,
        'credits': credits,
        'installmets': installments,
        'accounts': accounts
    }
    return render(request, 'bank/manager_page.html', context)


@login_required(login_url='login')
def financial_management(request):
    form = ManagementForm()
    if request.method == 'POST':
        form = ManagementForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            acc = data['account']
            dep = data['deposit']
            cred = data['credit']
            instl = data['installment']
            if acc:
                acc.block_status = data['account_block_status']
                acc.save()
            if dep:
                dep.block_status = data['deposit_block_status']
                dep.save()
            if cred:
                cred.credit_status = data['credit_status']
                cred.save()

            if instl:
                instl.installment_status = data['installment_status']
                instl.save()
    context = {'form': form}
    return render(request, 'bank/management.html', context)


@login_required(login_url='login')
def client_info(request):
    accounts = Account.objects.all()
    deposits = Deposit.objects.all()
    credits = Credit.objects.all()
    installments = Installment.objects.all()
    blocking_acc = False
    blocking_dep = False
    for acc in accounts:
        if acc.block_status:
            blocking_acc = True
    for dep in deposits:
        if dep.block_status:
            blocking_dep = True

    context = {
        'deposits': deposits,
        'credits': credits,
        'installmets': installments,
        'accounts': accounts,
        'block_acc': blocking_acc,
        'block_dep': blocking_dep,
    }

    return render(request, 'bank/client_info.html', context)


@login_required(login_url='login')
def money_transaction(request):
    form = TransactionForm()
    sender_acc = Account.objects.all().get(user=request.user)

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            ben_acc = data['beneficiary_account']
            sum = data['sum']

            if sum > sender_acc.sum:
                return HttpResponse('Hey, insufficient funds!')
            if ben_acc == sender_acc:
                return HttpResponse('Come on, you can\'t transfer money to yourself')

            sender_acc.sum -= sum
            sender_acc.save()
            ben_acc.sum += sum
            ben_acc.save()

    context = {
        'form': form,
        'sender_acc': sender_acc,
    }

    if freezing():
        return HttpResponse('Is Freezing a joke for U???')

    return render(request, 'bank/money_transaction.html', context)


@login_required(login_url='login')
def open_account(request):

    if request.method == 'POST':
        form = OpenAccountForm(request.POST)

        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
    else:
        form = OpenAccountForm()

    if freezing():
        return HttpResponse('Is Freezing a joke for U???')

    return render(request, 'bank/open_account.html', {'form': form})


@login_required(login_url='login')
def open_deposit(request):

    if request.method == 'POST':
        form = OpenDepositForm(request.POST)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
    else:
        form = OpenDepositForm()

    if freezing():
        return HttpResponse('Is Freezing a joke for U???')

    return render(request, 'bank/open_deposit.html', {'form': form})


@login_required(login_url='login')
def apply_for_credit(request):

    if request.method == 'POST':
        form = ApplyForCreditForm(request.POST)

        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.save()
    else:
        form = ApplyForCreditForm()

    if freezing():
        return HttpResponse('Is Freezing a joke for U???')

    return render(request, 'bank/apply_for_credit.html', {'form': form})


@login_required(login_url='login')
def apply_for_installment(request):

    if request.method == 'POST':
        form = ApplyForInstallmentForm(request.POST)

        if form.is_valid():
            installment = form.save(commit=False)
            installment.user = request.user
            installment.save()
    else:
        form = ApplyForInstallmentForm()

    if freezing():
        return HttpResponse('Is Freezing a joke for U???')

    return render(request, 'bank/apply_for_installment.html', {'form': form})


def freezing():
    frz = Economics.objects.all().get(freeze_status=True)
    return True if frz else False
