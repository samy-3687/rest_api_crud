from django.db import models

# Create your models here.
class Products(models.Model):
    prdid = models.IntegerField()
    prdname = models.CharField(max_length = 30)
    prdcat = models.CharField(max_length = 30)
    prdspec = models.CharField(max_length = 30)
    prdprice = models.IntegerField()
