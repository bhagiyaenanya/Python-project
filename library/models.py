from django.db import models
from django.utils.timezone import now




class registermodel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.IntegerField()
    mblenum = models.BigIntegerField()
    email = models.EmailField(max_length=400)
    gender = models.CharField(max_length=200)

class book_details(models.Model):
    bookname = models.CharField(max_length=300)
    code = models.IntegerField()
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=600)
    status =  models.CharField(max_length=600)
    created_by = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=600)
    updated_date = models.DateTimeField(default=now)

class order_detail(models.Model):
    bookid = models.ForeignKey(book_details,on_delete=models.SET_NULL,null=True)
    count = models.IntegerField()
    price = models.IntegerField()
    delivery_date = models.DateTimeField(default=now)
    status = models.CharField(max_length=600)
    created_by = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=now)
    updated_by = models.CharField(max_length=600)
    updated_date = models.DateTimeField(default=now)

