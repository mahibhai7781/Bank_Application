from django.contrib import admin
from Bank.models import Bank_Details, Transact_Details
# Register your models here.


class BankAdmin(admin.ModelAdmin):
    list_display = ['Account_Number', 'Name', 'Father_Name', 'Amount', 'Mobile', 'Gender',
                    'DOB', 'Address', 'City', 'State', 'Pin', 'Religion']


admin.site.register(Bank_Details, BankAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['Account', 'Pin', 'Amount', 'Debit_Credit', 'date']


admin.site.register(Transact_Details, TransactionAdmin)
