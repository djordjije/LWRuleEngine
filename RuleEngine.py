from Resources.Classes import *
from business_rules import run_all
from rule_maker import make_rules, read_csv

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

p = Product()
print p.current_inventory
print p.days_last_sold
p.days_last_sold = 4
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
