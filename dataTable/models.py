from django.db import models

# Create your models here.
class company(models.Model):
    date = models.CharField(max_length=100, null=True)
    trade_name = models.CharField(max_length=100, null=True)
    high = models.FloatField(max_length=100, null=True)
    low = models.FloatField(max_length=100, null=True)
    open = models.FloatField(max_length=100, null=True)
    close = models.FloatField(max_length=100, null=True)
    volume = models.IntegerField(null=True)