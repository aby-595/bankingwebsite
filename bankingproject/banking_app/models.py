# banking/models.py
from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

class Account(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    materials_provided = models.ManyToManyField('Material')

class Material(models.Model):
    name = models.CharField(max_length=100)
