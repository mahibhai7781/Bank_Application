from django.contrib import admin
from ATM.models import ATM_Details
# Register your models here.


class AtmAdmin(admin.ModelAdmin):
    list_display = ['Account_Number', 'Pin_Number', 'Amount', 'Mobile']


admin.site.register(ATM_Details,AtmAdmin)
