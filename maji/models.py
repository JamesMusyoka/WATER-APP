from django.db import models


class Suppliers(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length = 10,blank =True)
    suppliers_pic = models.ImageField(upload_to='suppliers/', default='image')
    email = models.EmailField()
    national_id = models.IntegerField(null=True)

    def save_suppliers(self):
        self.save()

    def update_suppliers(self):
        self.save()

    def create_suppliers(self):
        self.save()

    def __str__(self):
        return self.first_name

class Customers(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length = 10,blank =True)
    customers_pic = models.ImageField(upload_to='suppliers/', default='image')
    email = models.EmailField()
    national_id = models.IntegerField(null=True)

    def save_customers(self):
        self.save()

    def delete_customers(self):
        self.save()

    def create_customers(self):
        self.save()

    def update_customers(self):
        self.save()

    def __str__(self):
        return self.first_name

class Water(models.Model):
    location = models.CharField(max_length=50)
    litres = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def save_water(self):
        self.save()

    def delete_water(self):
        self.save()

