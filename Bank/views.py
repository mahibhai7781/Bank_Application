
from re import A
from sqlite3 import connect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Bank.models import Bank_Details,Transact_Details
from ATM.models import ATM_Details
import random

# Create your views here.


def home(request):
    return render(request, 'Bank/Home.html')


def bank_home(request):
    return render(request, 'Bank/bHome.html')


def atm_home(request):
    return render(request, 'ATM/Home.html')


def open_account(request):
    if request.method == 'POST':
        account = '283101000'
        random_number = str(random.randint(10000, 99999))
        account_number = account + random_number
        name = request.POST.get('cname')
        father_name = request.POST.get('fname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        religion = request.POST.get('religion')
        gender = request.POST.get('gender')
        amount = request.POST.get('amount')
        bank_data = Bank_Details.objects.all()
        for b_data in bank_data:
            if b_data.Name == name and b_data.Father_Name == father_name and b_data.Mobile == int(mobile) and str(b_data.DOB) == dob:
                return HttpResponse(f'''<div style="margin:auto;margin-top:50px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                <h3>Sorry, You can't open another A/C Because you are old customer in Bank. Please check</h3>
                <br><br><a href="/openAC" style="margin-left:250px;">Back</a>''')
                
        if int(amount) >= 1000:
            Bank_Details.objects.create(Name=name, Father_Name=father_name, Account_Number=account_number,
                                        Amount=amount, Mobile=mobile, Gender=gender, DOB=dob, Address=address,
                                        City=city, State=state, Pin=pin, Religion=religion)
            Transact_Details.objects.create(Account=account_number, Amount=amount, Debit_Credit='Credit')

            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:620px;height:800px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {name} in my bank A/C</h3>
                <h3>Your A/C Open Successfully in Bank</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>Customer Name :</th><td>{name}</td></tr>
                <tr><th>Father's Name :</th><td>{father_name}</td></tr>
                <tr><th>Date Of Birth :</th><td>{dob}</td></tr>
                 <tr><th>Gender :</th><td>{gender}</td></tr>
                <tr><th>Account No. :</th><td>{account_number}</td></tr>
                <tr><th>Amount :</th><td>{amount}</td></tr>
                <tr><th>Mobile No. :</th><td>{mobile}</td></tr>
                <tr><th>Address :</th><td>{address}</td></tr>
                <tr><th>Customer Name :</th><td>{city}</td></tr>
                <tr><th>Father's Name :</th><td>{state}</td></tr>
                <tr><th>Account No. :</th><td>{pin}</td></tr>
                <tr><th>Father's Name :</th><td>{religion}</td></tr>
            </table><br><br><a href="/openAC" style="margin-left:250px;">Back</a>''')

    else:
        return render(request, 'Bank/OpenAccount.html')


def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        account = request.POST.get('account')
        bank_data = Bank_Details.objects.all()
        for b_data in bank_data:
            if account == b_data.Account_Number:
                if int(amount)+1000 <= b_data.Amount:
                    total_amount = b_data.Amount-int(amount)
                    atm_detail = ATM_Details.objects.filter(Account_Number=account)
                    if atm_detail:
                        Bank_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                        ATM_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                        Transact_Details.objects.create(Account=b_data.Account_Number, Pin=atm_detail.Pin_Number,
                                                    Amount=int(amount), Debit_Credit='Debit')
                    else:
                        Bank_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                        Transact_Details.objects.create(Account=b_data.Account_Number,
                                                        Amount=int(amount), Debit_Credit='Debit')
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                 <h3>Withdraw Successfully from Your A/C</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>A/C Number :</th><td>{account}</td></tr>
                <tr><th>Withdraw Amount :</th><td>{amount}</td></tr>
                <tr><th>Total Amount :</th><td>{total_amount}</td></tr>
            </table><br><br><a href="/withdraw" style="margin-left:250px;">Back</a>''')
                
                else:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                <h3>Sorry, You do not have enough balence in your A/C. Please check</h3>
                <br><br><a href="/withdraw" style="margin-left:250px;">Back</a>''')

        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is wrong. Please check</h3>
                <br><br><a href="/withdraw" style="margin-left:250px;">Back</a>''')
                
    else:
        return render(request, 'Bank/Withdraw.html')


def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        account = request.POST.get('account')
        bank_data = Bank_Details.objects.all()
        for b_data in bank_data:
            if account == b_data.Account_Number:
                total_amount = b_data.Amount+int(amount)
                atm_detail = ATM_Details.objects.filter(Account_Number=account)
                if atm_detail:
                    Bank_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                    ATM_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                    Transact_Details.objects.create(Account=b_data.Account_Number, Pin=atm_detail.Pin_Number,
                                                    Amount=int(amount), Debit_Credit='Credit')
                else:
                    Bank_Details.objects.filter(Account_Number=account).update(Amount=total_amount)
                    Transact_Details.objects.create(Account=b_data.Account_Number,
                                                    Amount=int(amount), Debit_Credit='Credit')

                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                 <h3>Your Amount Deposit Successfully into A/C</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>A/C Number :</th><td>{account}</td></tr>
                <tr><th>Withdraw Amount :</th><td>{amount}</td></tr>
                <tr><th>Total Amount :</th><td>{total_amount}</td></tr>
            </table><br><br><a href="/deposit" style="margin-left:250px;">Back</a>''')
                
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is wrong. Please check</h3>
                <br><br><a href="/deposit" style="margin-left:250px;">Back</a>''')

    else:
        return render(request, 'Bank/Deposit.html')


def change_mobile(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        reason = request.POST.get('reason')
        old_mobile = request.POST.get('oMobile')
        new_mobile = request.POST.get('nMobile')
        bank_data = Bank_Details.objects.all()
        for b_data in bank_data:
            if account == b_data.Account_Number:
                if old_mobile == new_mobile:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                        width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                        <h3 style='text-align:center;background-color:purple; color:white'>
                        Welcome in my bank A/C</h3>
                        <h3>Sorry, your  both Mobile number is Same. Please check</h3>
                        <br><br><a href="/changeMobile" style="margin-left:250px;">Back</a>''')

                elif len(old_mobile) != 10 or len(new_mobile) != 10:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black;
                        width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                        <h3 style='text-align:center;background-color:purple; color:white'>
                        Welcome in my bank A/C</h3>
                        <h3>Entered mobile number must be 10 digit. Please check once your entered mobie number</h3>
                        <br><br><a href="/changeMobile" style="margin-left:250px;">Back</a>''')

                elif int(old_mobile) == b_data.Mobile:
                    Bank_Details.objects.filter(Account_Number=account).update(Mobile=int(new_mobile))
                    ATM_Details.objects.filter(Account_Number=account).update(Mobile=int(new_mobile))
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                 <h3>Your Mobile Number change Successfully in Bank</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>A/C Number :</th><td>{b_data.Account_Number}</td></tr>
                <tr><th>Total Amount :</th><td>{b_data.Amount}</td></tr>
                <tr><th>Mobile No. :</th><td>{new_mobile}</td></tr>
            </table><br><br><a href="/deposit" style="margin-left:250px;">Back</a>''')
                
                else:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                    width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                    <h3 style='text-align:center;background-color:purple; color:white'>
                    Welcome in my bank A/C</h3>
                    <h3>Sorry, This Mobile number "{old_mobile}" is not attached from your Account . Please check</h3>
                    <br><br><a href="/changeMobile" style="margin-left:250px;">Back</a>''')

        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is wrong. Please check</h3>
                <br><br><a href="/changeMobile" style="margin-left:250px;">Back</a>''')
            
    else:
        return render(request, 'Bank/ChangeMobileNo.html')


def balance_enq(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        bank_data = Bank_Details.objects.all()
        for b_data in bank_data:
            if account == b_data.Account_Number:
                amount = b_data.Amount
                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>A/C Number :</th><td>{account}</td></tr>
                <tr><th>Amount :</th><td>{amount}</td></tr>
            </table><br><br><a href="/balanceEnq" style="margin-left:250px;">Back</a>''')
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is wrong. Please check</h3>
                <br><br><a href="/balanceEnq" style="margin-left:250px;">Back</a>''')
            
    else:
        return render(request, 'Bank/BalanceEnq.html')


def fund_transfer(request):
    if request.method == 'POST':
        account_num1 = request.POST.get('account1')
        account_num2 = request.POST.get('account2')
        amount = request.POST.get('amount')
        bank_data = Bank_Details.objects.all()
        if account_num1 == account_num2:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your both A/C number is same. Please check</h3>
                <br><br><a href="/fundTransfer" style="margin-left:250px;">Back</a>''')
            
        else:
            for b_data1 in bank_data:
                if account_num1 == b_data1.Account_Number:
                    for b_data2 in bank_data:
                        if account_num2 == b_data2.Account_Number:
                            if int(amount)+1000 <= b_data1.Amount:
                                total_amount1 = b_data1.Amount-int(amount)
                                total_amount2 = b_data2.Amount+int(amount)
                                atm_detail1 = ATM_Details.objects.get(Account_Number=account_num1)
                                atm_detail2 = ATM_Details.objects.get(Account_Number=account_num2)
                                Bank_Details.objects.filter(Account_Number=account_num1).update(Amount=total_amount1)
                                Bank_Details.objects.filter(Account_Number=account_num2).update(Amount=total_amount2)
                                ATM_Details.objects.filter(Account_Number=account_num1).update(Amount=total_amount1)
                                ATM_Details.objects.filter(Account_Number=account_num2).update(Amount=total_amount2)
                                Transact_Details.objects.create(Account=b_data1.Account_Number,
                                                                Pin=atm_detail1.Pin_Number, Amount=int(amount), Debit_Credit='Debit')
                                Transact_Details.objects.create(Account=b_data2.Account_Number,
                                                                Pin=atm_detail2.Pin_Number,Amount=int(amount), Debit_Credit='Credit')
                                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data1.Name} in my bank A/C</h3>
                 <h3>Your Fund transfer Successfully into A/C</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>A/C Number :</th><td>{account_num1}</td></tr>
                <tr><th>Withdraw Amount :</th><td>{amount}</td></tr>
                <tr><th>Total Amount :</th><td>{total_amount1}</td></tr>
            </table><br><br><a href="/deposit" style="margin-left:250px;">Back</a>''')
                
                            else:
                                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; 
                border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data1.Name} in my bank A/C</h3>
                <h3>Sorry, You do not have enough balence in your A/C. Please check</h3>
                <br><br><a href="/fundTransfer" style="margin-left:250px;">Back</a>''')
                
                    else:
                        return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data1.Name} in my bank A/C</h3>
                <h3>Sorry, Destination A/C does not exists. Please check</h3>
                <br><br><a href="/fundTransfer" style="margin-left:250px;">Back</a>''')
                           
            else:
                return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is not exists in Bank. Please check</h3>
                <br><br><a href="/fundTransfer" style="margin-left:250px;">Back</a>''')
            
    else:
        return render(request, 'Bank/FundTransfer.html')


def close_account(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        reason = request.POST.get('reason')
        mobile = request.POST.get('mobile')
        bank_data = Bank_Details.objects.all()
        for b_data in bank_data:
            if account == b_data.Account_Number:
                if int(mobile) == b_data.Mobile:
                    Bank_Details.objects.filter(Account_Number=account).delete()
                    ATM_Details.objects.filter(Account_Number=account).delete()
                    Transact_Details.objects.filter(Account=account).delete()
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:620px;height:800px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome {b_data.Name} in my bank A/C</h3>
                <h3>Your A/C Closed Successfully from Bank</h3>
                <table style="margin:auto;font-size:25px">
                <tr><th>Customer Name :</th><td>{b_data.Name}</td></tr>
                <tr><th>Father's Name :</th><td>{b_data.Father_Name}</td></tr>
                <tr><th>Date Of Birth :</th><td>{b_data.DOB}</td></tr>
                 <tr><th>Gender :</th><td>{b_data.Gender}</td></tr>
                <tr><th>Account No. :</th><td>{b_data.Account_Number}</td></tr>
                <tr><th>Amount :</th><td>{b_data.Amount}</td></tr>
                <tr><th>Mobile No. :</th><td>{b_data.Mobile}</td></tr>
                <tr><th>Address :</th><td>{b_data.Address}</td></tr>
                <tr><th>Customer Name :</th><td>{b_data.City}</td></tr>
                <tr><th>Father's Name :</th><td>{b_data.State}</td></tr>
                <tr><th>Account No. :</th><td>{b_data.Pin}</td></tr>
                <tr><th>Father's Name :</th><td>{b_data.Religion}</td></tr>
            </table><br><br><a href="/closeAC" style="margin-left:250px;">Back</a>''')
            
                else:
                    return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                        width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                        <h3 style='text-align:center;background-color:purple; color:white'>
                        Welcome in my bank A/C</h3>
                        <h3>Sorry, This Mobile number "{mobile}" is not attached from your Account . Please check</h3>
                        <br><br><a href="/closeAC" style="margin-left:250px;">Back</a>''')
                    
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is wrong. Please check</h3>
                <br><br><a href="/closeAC" style="margin-left:250px;">Back</a>''')
            
                
    else:
        return render(request, 'Bank/CloseBank.html')


def transaction(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        transaction_data = Transact_Details.objects.all()
        for data in transaction_data:
            if account == data.Account:
                info = Transact_Details.objects.filter(Account=account)
                return render(request, 'Bank/Passbook.html', {'info': info})
        else:
            return HttpResponse(f'''<div style="margin:auto;margin-top:100px; border: 2px solid black; 
                width:600px;height:400px;font-size:25px; background-color:lightgrey; border-radius:30px;">
                <h3 style='text-align:center;background-color:purple; color:white'>
                Welcome in my bank A/C</h3>
                <h3>Sorry, your A/C number is wrong. Please check</h3>
                <br><br><a href="/transaction" style="margin-left:250px;">Back</a></div>''')                                 
                
    else:
        return render(request, 'Bank/Transaction.html')
    
