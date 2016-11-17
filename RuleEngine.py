from Resources.Classes import *
from business_rules import run_all
from rule_maker import make_rules
import csv


rules = make_rules()
print rules
output_file = open('C:/Users/George/Dropbox/price_output.csv', 'wb')
price_output = csv.writer(output_file)
price_output.writerow(['stock_item_id', 'bc_id', 'sku', 'old_price', 'new_price', 'change'])
output_file.close()

with open('C:/Users/George/Dropbox/rule_engine_data.csv') as csv_file:
    product_csv = csv.reader(csv_file)
    next(product_csv)
    for row in product_csv:
        input_list = [row[0], row[1], row[2], row[3], int(row[4])]
        input_list.append(int(row[5])) if row[5] != '' else input_list.append(-1)  # days last sold
        input_list.append(float(row[6])) if row[6] != '' else input_list.append(-1)  # last sold price
        input_list.append(float(row[7])) if row[7] != '' else input_list.append(0)  # weight
        input_list.append(int(row[8]))  # available
        input_list.append(round(float(row[9]), 2)) if row[9] != '' else input_list.append(-1)  # unit cost
        input_list.append(float(row[10])) if row[10] != '' else input_list.append(-1)  # retail price
        input_list.append(int(row[11])) if row[11] != '' else input_list.append(-1)  # inventory went +
        input_list.append(int(row[12])) if row[12] != '' else input_list.append(-1)  # last price update
        input_list.append(int(row[13])) if row[13] != '' else input_list.append(-1)  # days ago created
        input_list.append(int(row[14])) if row[14] != '' else input_list.append(-1)  # bc_id

        print input_list

        # input_list = ['TEST', 'test-item-id', 'test product title', 'apple watches', 10, 5, 10.5, 4, 2, 5.2, 10.5, 0, 4, 100]
        p = Product(*input_list)

        product = ProductVariables(p)
        # print product.current_inventory()
        # print product.days_last_sold()
        # print type(product.days_last_sold())
        # print product.category()

        run_all(rule_list=rules,
                defined_variables=ProductVariables(p),
                defined_actions=ProductActions(p),
                stop_on_first_trigger=True
                )

        output_file.close()
