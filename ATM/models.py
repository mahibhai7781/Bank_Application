from django.db import models

# Create your models here.


class ATM_Details(models.Model):
    Account_Number = models.CharField(max_length=14,primary_key=True)
    Pin_Number = models.IntegerField(null=True,unique=True)
    Mobile = models.BigIntegerField(null=True)
    Amount = models.BigIntegerField(null=True)
    
