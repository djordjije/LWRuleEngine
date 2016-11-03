from business_rules.variables import *
from business_rules.actions import *
from business_rules.operators import *


class Product:
    def __init__(self):
        self.current_inventory = 24
        self.days_last_sold = 5
        self.price = 10.00


class ProductVariables(BaseVariables):
    def __init__(self, product):
        self.product = product

    @numeric_rule_variable
    def current_inventory(self):
        return self.product.current_inventory

    @numeric_rule_variable
    def days_last_sold(self):
        return self.product.days_last_sold


class ProductActions(BaseActions):
    def __init__(self, product):
        self.product = product

    @rule_action(params={'sales_percentage': FIELD_NUMERIC})
    def increase_price(self, sales_percentage):
        self.product.new_price = (1.0 + sales_percentage) * self.product.price
        print 'Price went up from ' + str(self.product.price) + ' to ' + str(self.product.new_price)