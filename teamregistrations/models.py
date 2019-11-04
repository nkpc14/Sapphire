from django.db import models

class PaymentData(models.Model):
    porderid = models.CharField(max_length=100)
    pmid = models.CharField(max_length=100)
    ptxnid = models.CharField(max_length=100)
    ptxnamount = models.CharField(max_length=100)
    ppaymentmode = models.CharField(max_length=100,blank = True, null = True,default = None)
    pcurrency = models.CharField(max_length=100,blank = True, null = True,default = None)
    ptxndate = models.CharField(max_length=100)
    pstatus = models.CharField(max_length=100)
    prespcode = models.CharField(max_length=100)
    prespmeg = models.CharField(max_length=500)
    pgatewayname = models.CharField(max_length=100,blank = True, null = True,default = None)
    pbanktxnid = models.CharField(max_length=100,blank = True, null = True,default = None)
    pbankname = models.CharField(max_length=100,blank = True, null = True,default = None)








