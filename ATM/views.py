from ctypes.wintypes import PINT
from django.shortcuts import render
from django.http import HttpResponse
from ATM.models import ATM_Details
from Bank.models import Bank_Details, Transact_Details
import random

# Create your views here.


def home(request):
    return render(request, 'ATM/Home.html')


def generate_pin(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        mobile = request.POST.get('mobile')
        otp = request.POST.get('otp')
        bank_data = Bank_Details.objects.all()
        atm_data =ATM_Details.objects.all()
        for a_data in atm_data:
            if a_data.Account_Number == account:
                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                <h3>Sorry, your ATM Pin Number generated already . Please check</h3>
                <br><br><a href="/atm/generatePin" style="margin-left:250px;">Back</a>''')  
        for b_data in bank_data:
            if account == b_data.Account_Number:
                if int(mobile) == b_data.Mobile:
                    pin_num = random.randint(1000, 10000)
                    total_amount = b_data.Amount
                    ATM_Details.objects.create(Account_Number=account, Pin_Number=pin_num, Mobile=mobile,
                                               Amount=total_amount)
                    Transact_Details.objects.filter(Account=account).update(Pin=pin_num)
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                    width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                    <h3 style='text-align:center;background-color:purple; color:white'>
                    Welcome in my ATM Application</h3>
                    <h3>ATM Pin generate Successfully</h3>
                    <table style="margin:auto;font-size:25px">
                    <tr><th>Account Number :</th><td>{account}</td></tr>
                    <tr><th>Total Amount :</th><td>{total_amount}</td></tr>
                    <tr><th>Pin Number :</th><td>{pin_num}</td></tr>
                    </table><br><br><a href="/atm/generatePin" style="margin-left:250px;">Back</a>''')
                else:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                <h3>Sorry, your Mobile number is not exists in your Bank A/C. Please check</h3>
                <br><br><a href="/atm/generatePin" style="margin-left:250px;">Back</a>''')

        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                <h3>Sorry, your A/C number is not exists in Bank. Please check</h3>
                <br><br><a href="/atm/generatePin" style="margin-left:250px;">Back</a>''')
                                  
    else:
        sotp=random.randint(100000, 1000000)
    
        return render(request, 'ATM/GeneratePin.html', {'sotp': sotp})


def withdraw(request):
    if request.method == 'POST':
        pin_number = request.POST.get('pin')
        amount = request.POST.get('amount')
        atm_data = ATM_Details.objects.all()
        for a_data in atm_data:
            if int(pin_number) == a_data.Pin_Number:
                if int(amount)+1000 <= a_data.Amount:
                    account = a_data.Account_Number
                    total_amount = a_data.Amount-int(amount)
                    ATM_Details.objects.filter(Pin_Number=pin_number).update(Amount=total_amount)
                    Bank_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                    Transact_Details.objects.create(Account=account, Pin=int(pin_number), Amount=int(amount),
                                                    Debit_Credit='Debit')
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                 <h3>Withdraw Successfully from Your A/C</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>Withdraw Amount :</th><td>{amount}</td></tr>
                <tr><th>Total Amount :</th><td>{total_amount}</td></tr>
            </table><br><br><a href="/atm/withdraw" style="margin-left:250px;">Back</a>''')
                
                else:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                <h3>Sorry, You do not have enough balence in your A/C. Please check</h3>
                <br><br><a href="/atm/withdraw" style="margin-left:250px;">Back</a>''')

        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your Pin number is wrong. Please check</h3>
                <br><br><a href="/atm/withdraw" style="margin-left:250px;">Back</a>''')
                
    else:
        return render(request, 'ATM/Withdraw.html')


def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        pin = request.POST.get('pin')
        atm_data = ATM_Details.objects.all()
        for a_data in atm_data:
            if int(pin) == a_data.Pin_Number:
                total_amount = a_data.Amount+int(amount)
                account = a_data.Account_Number
                ATM_Details.objects.filter(Pin_Number=pin).update(Amount=total_amount)
                Bank_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                Transact_Details.objects.create(Account=account, Pin=int(pin), Amount=int(amount), Debit_Credit='Credit')
                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application </h3>
                 <h3>Your Amount Deposit Successfully into A/C</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>Deposit Amount :</th><td>{amount}</td></tr>
                <tr><th>Total Amount :</th><td>{total_amount}</td></tr>
            </table><br><br><a href="/atm/deposit" style="margin-left:250px;">Back</a>''')
                
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                <h3>Sorry, your ATM number is wrong. Please check</h3>
                <br><br><a href="/atm/deposit" style="margin-left:250px;">Back</a>''')

    else:
        return render(request, 'ATM/Deposit.html')


def balance_enq(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        atm_data = ATM_Details.objects.all()
        for data in atm_data:
            if int(pin) == data.Pin_Number:
                amount = data.Amount
                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my ATM Application</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th> Total Amount :</th><td>{amount}</td></tr>
            </table><br><br><a href="/atm/balanceEnq" style="margin-left:250px;">Back</a>''')
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your ATM Pin number is wrong. Please check</h3>
                <br><br><a href="/atm/balanceEnq" style="margin-left:250px;">Back</a>''')
            
    else:
        return render(request, 'ATM/BalanceEnq.html')


def transaction(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        mobile = request.POST.get('mobile')
        transaction_data = Transact_Details.objects.all()
        for t_data in transaction_data:
            if int(pin) == t_data.Pin:
                info = Transact_Details.objects.filter(Pin=int(pin))
                return render(request, 'ATM/Passbook.html', {'info': info})
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your ATM Pin number is wrong. Please check</h3>
                <br><br><a href="/atm/transaction" style="margin-left:250px;">Back</a></div>''')                                 
                
    else:
        return render(request, 'ATM/Transaction.html')


def about(request):
    return render(request, 'ATM/About.html')


def other(request):
    return render(request, 'ATM/Other.html')
