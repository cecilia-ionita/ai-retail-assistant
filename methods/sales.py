def calculate_sale_value(quantity, unit_price):
    sale_value = quantity * unit_price
    return sale_value


def calculate_profit(sale_value, cost):
    profit =  sale_value -cost
    return profit


def calculate_profit_margin(sale_value, cost):
    profit = calculate_profit(sale_value, cost)
    profit_margin = profit / sale_value
    return profit_margin