from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('Bhome', views.bank_home),
    path('Ahome', views.atm_home),
    path('openAC', views.open_account),
    path('withdraw', views.withdraw),
    path('deposit', views.deposit),
    path('balanceEnq', views.balance_enq),
    path('changeMobile', views.change_mobile),
    path('fundTransfer', views.fund_transfer),
    path('closeAC', views.close_account),
    path('transaction', views.transaction),

]

