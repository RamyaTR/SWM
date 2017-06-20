# Create your models here.

from django.db import models
from django.utils import timezone
from datetime import datetime

AUTHORIZATION = (
    ('1', 'Waste Processing'),
    ('2', 'Recycling'),
    ('3', 'Treatment'),
    ('4', 'Disposal at landfill')
    )

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Form1(models.Model):
    user = models.ForeignKey('auth.User')
    address =  models.CharField(max_length=300)
    fax = models.IntegerField(max_length=20)
    nodal = models.CharField(max_length=100)
    authorization = models.CharField(max_length=25, choices = AUTHORIZATION, default='1')
    
    site_clear = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    env_clear = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    consent = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    agreement = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    investment = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    
    quant_recycle = models.IntegerField(max_length=10)
    quant_treat = models.IntegerField(max_length=10)
    quant_dispose = models.IntegerField(max_length=10)
    util = models.CharField(max_length=1000)
    method_dis = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    quant_leach = models.IntegerField(max_length=10)
    treatleach = models.CharField(max_length=1000)
    measure = models.CharField(max_length=1000)
    safety = models.CharField(max_length=1000)
    details = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)

    no_sw = models.IntegerField(max_length=10)
    quant_sw = models.IntegerField(max_length=10)
    details_sw = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
    op_sw = models.CharField(max_length=1000)
    landfill_sw = models.CharField(max_length=1000)
    poll = models.CharField(max_length=1000)

    date = models.DateTimeField(default=datetime.now)

    info = models.CharField(max_length=1000, null = True, blank=True)


class Form3(models.Model):
    city = models.CharField(max_length=100)
    pop = models.IntegerField(max_length=10000)
    area = models.IntegerField(max_length=10)
    name_loc = models.CharField(max_length=20)
    fax_loc=models.IntegerField(max_length=10)

    name_op = models.CharField(max_length=20)

    name_off = models.CharField(max_length=20)

    no_hh = models.IntegerField(max_length=1000)
    no_nr = models.IntegerField(max_length=1000)
    no_e = models.IntegerField(max_length=1000)

    quant_sw = models.IntegerField(max_length=100)
    es_sw = models.IntegerField(max_length=100)
    quant_d = models.IntegerField(max_length=100)
    per_cap =  models.IntegerField(max_length=100)
    procc_sw = models.IntegerField(max_length=100)
    dis_sw = models.IntegerField(max_length=100)

    p_bins = models.IntegerField(max_length=2)
    p_ins = models.IntegerField(max_length=2)
    p_street = models.IntegerField(max_length=2)
    p_sw = models.IntegerField(max_length=2)
    p_seg = models.IntegerField(max_length=2)

    p_d2d = models.IntegerField(max_length=2)
    p_hh = models.IntegerField(max_length=2)
    p_nr = models.IntegerField(max_length=2)
    p_d = models.IntegerField(max_length=2)
    p_motor = models.IntegerField(max_length=2)
    p_hcart = models.IntegerField(max_length=2)
    p_other = models.IntegerField(max_length=2)

    ww_waste = models.FileField(upload_to='documents/%Y/%m/%d', null = True, blank=True)
