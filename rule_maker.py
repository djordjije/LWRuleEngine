import csv, json


def read_csv():
    raw_rules = []
    f = open('C:/Users/George/Dropbox/rules.csv')
    csv_file = csv.reader(f)
    for row in csv_file:
        count = 0
        while count < len(row):
            raw_rules.append(row[count].strip())
            count += 1
    rules = []
    for item in raw_rules:
        if item.lower() == 'parameter':
            continue
        if str(item).startswith('#'):
            continue
        if item == '':
            continue
        rules.append(item)
    return rules


# list = read_csv()
# list = ['rule',"CONDITION", "days_last_sold", "greater_than", 4,"CONDITION", "created", "less_than", 5, 'action',
# 'increase_price', 'sales_percentage', 0.1, 'rule',"CONDITION", "days_last_sold", "greater_than", 4,"CONDITION",
# "created", "less_than", 5, 'action', 'increase_price', 'sales_percentage', 0.1]
# rules = []


def make_conditions(cond_list):
    conditions = []
    k = 0
    while k < len(cond_list):
        if cond_list[k].upper() == "CONDITION":
            condition = {"name": cond_list[k+1], "operator": cond_list[k+2], "value": float(cond_list[k+3])}
            k += 4
            conditions.append(condition)
    return conditions


def make_actions(act_list):
    actions = []
    m = 0
    while m < len(act_list):
        if act_list[m].upper() == 'ACTION':
            action = {'name': act_list[m+1], 'params': {act_list[m+2]: float(act_list[m+3])}}
            m += 4
            actions.append(action)
    return actions


def make_rules():
    rules = []
    rule_list = read_csv()
    i = 0
    # next_rule = 0
    while len(rule_list) != 0:
        if rule_list[i].upper() == 'RULE':
            rule_list.pop(i)
            if 'rule' not in rule_list:
                print 'last rule getting processed'
                action = rule_list.index('action')
                conditions = rule_list[0:action]
                actions = rule_list[action:]
                rule_list = []
            else:
                print 'rule getting processed'
                next_rule = rule_list.index('rule')
                action = rule_list.index('action')
                conditions = rule_list[0:action]
                actions = rule_list[action:next_rule]
                rule_list = rule_list[next_rule:]
            rules.append({'conditions': {'all': make_conditions(conditions)}, 'actions': make_actions(actions)})
    print rules
    return rules

make_rules()