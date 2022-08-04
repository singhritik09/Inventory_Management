# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    aadhar = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Inventory(models.Model):
    inid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    quantity_sold = models.IntegerField()
    sales = models.IntegerField()
    stock_date = models.DateField()
    last_sale = models.DateField()

    class Meta:
        managed = False
        db_table = 'inventory'
