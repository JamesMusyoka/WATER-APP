from django.test import TestCase
from .models import *

class SuppliersTestClass(TestCase):

    def setUp(self):
        self.james = Suppliers(first_name = 'James', email = 'jamesmu475@gmail.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.james,Suppliers))


    def test_save_method(self):
        self.james.save_suppliers()
        suppliers = Suppliers.objects.all()
        self.assertTrue(len(suppliers) > 0)

    def test_update_suppliers(self):
        self.james.update_suppliers()
        suppliers = Suppliers.objects.all()
        self.assertTrue(len(suppliers) == 1)

    def test_create_suppliers(self):
        self.james.create_suppliers()
        suppliers = Suppliers.objects.all()
        self.assertTrue(len(suppliers) > 0)

class CustomersTestClass(TestCase):

    def setUp(self):
        self.rony = Customers(first_name = 'Rony', email='rony@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.rony,Customers))


    def test_save_method(self):
        self.rony.save_customers()
        customers = Customers.objects.all()
        self.assertTrue(len(customers) > 0)

    def test_delete_customers(self):
        self.rony.delete_customers()
        customers = Customers.objects.all()
        self.assertFalse(len(customers) == 0)

    def test_create_customers(self):
        self.rony.create_customers()
        customers = Customers.objects.all()
        self.assertTrue(len(customers) > 0)

    def test_update_customers(self):
        self.rony.update_customers()
        customers = Customers.objects.all()
        self.assertTrue(len(customers) == 1)


class WaterTestClass(TestCase):

    def setUp(self):
        self.kibera = Water(location = 'Kibera')

    def test_instance(self):
        self.assertTrue(isinstance(self.kibera,Water))

    def test_save_method(self):
        self.kibera.save_water()
        water = Water.objects.all()
        self.assertTrue(len(water) > 0)

    def test_delete_water(self):
        self.kibera.delete_water()
        water= Water.objects.all()
        self.assertFalse(len(water) == 0)