from TestFolder.Classes import TestA
from business_rules.variables import *
from business_rules.actions import *
from business_rules import run_all
from business_rules.operators import *
from rule_maker import make_rules, read_csv


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

rules_old = [
    {"conditions": {
        "all": [
            {
            "operator": "greater_than",
            "name": "days_last_sold",
            "value": 4,
             }
        ]},
    "actions": [
        {"name": "increase_price",
         "params": {"sales_percentage": 0.1},
         }
    ]
    }
]

rules = make_rules()

p = TestA()
print p.current_inventory
print p.days_last_sold
print type(p.days_last_sold)

product = ProductVariables(p)
print product.current_inventory()
print product.days_last_sold()
print type(product.days_last_sold())

run_all(rule_list=rules,
        defined_variables=ProductVariables(p),
        defined_actions=ProductActions(p),
        stop_on_first_trigger=True
        )
