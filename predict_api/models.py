from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    company = models.CharField(max_length=40)
    last_update = models.DateField()

class DailyPrice(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()
    open = models.BigIntegerField()
    high = models.BigIntegerField()
    low = models.BigIntegerField()
    close = models.BigIntegerField()
    diff = models.BigIntegerField()
    volume = models.BigIntegerField()


