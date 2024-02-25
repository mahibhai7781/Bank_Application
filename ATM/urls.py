from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('atm/generatePin', views.generate_pin),
    path('atm/withdraw', views.withdraw),
    path('atm/deposit', views.deposit),
    path('atm/balanceEnq', views.balance_enq),
    path('atm/transaction', views.transaction),
    path('atm/about', views.about),
    path('atm/other', views.other),
   ]
