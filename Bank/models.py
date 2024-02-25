from msilib.schema import tables
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
import pytz
from django.utils import timezone

# Create your models here.


class Bank_Details(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Father_Name = models.CharField(max_length=100, null=True)
    Account_Number = models.CharField(max_length=14, primary_key=True)
    Amount = models.BigIntegerField(null=True)
    Mobile = models.BigIntegerField(null=True)
    Gender = models.CharField(max_length=6, null=True)
    DOB = models.DateField(null=True)
    Address = models.CharField(max_length=300, null=True)
    City = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Pin = models.IntegerField(null=True)
    Religion = models.CharField(max_length=50, null=True)


class Transact_Details(models.Model):
    Account = models.CharField(max_length=14)
    Pin = models.IntegerField(null=True)
    Amount = models.IntegerField()
    Debit_Credit = models.CharField(max_length=7)
    date = models.DateTimeField(default=timezone.localtime)
    
    