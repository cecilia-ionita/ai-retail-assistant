def calculate_sale_value(quantity, unit_price):
    if quantity < 0 or unit_price < 0:
        raise ValueError("Quantity and unit price must be non-negative.")

    sale_value = quantity * unit_price
    return sale_value

def calculate_profit(sale_value, cost):
    if sale_value < 0:
        raise ValueError("Sale value must be non-negative.")

    if cost < 0:
        raise ValueError("Cost must be non-negative.")

    profit = sale_value - cost
    return profit

def calculate_profit_margin(sale_value, cost):
    if sale_value == 0:
        raise ValueError("Sale value cannot be zero.")
    
    profit = calculate_profit(sale_value, cost)
    profit_margin = profit / sale_value * 100
    return profit_margin

def calculate_discounted_price(sale_value, discount_percent):
    if discount_percent < 0 or discount_percent >100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    discount_value = sale_value * discount_percent / 100
    discounted_price = sale_value - discount_value
    return discounted_price

def calculate_price_with_vat(sale_value, vat_percent):
    if vat_percent < 0 or vat_percent > 100:
        raise ValueError("VAT percentage must be between 0 and 100.")
    vat_value = sale_value * vat_percent / 100
    price_with_vat = sale_value + vat_value
    return price_with_vat

def calculate_vat_value(discounted_price, vat_percent):
    if vat_percent < 0 or vat_percent > 100:
        raise ValueError("VAT percentage must be between 0 and 100.")
    vat_value = discounted_price * vat_percent / 100
    return vat_value

def calculate_order_initial_value(quantity, unit_price):
    if quantity < 0 or unit_price < 0:
        raise ValueError("Quantity and unit price must be non-negative.")
    
    initial_value = quantity * unit_price
    return initial_value

def calculate_final_price(quantity, unit_price, discount_percent, vat_percent):
    initial_value = calculate_order_initial_value(quantity, unit_price)
    discounted_price = calculate_discounted_price(initial_value, discount_percent)
    final_price = calculate_price_with_vat(discounted_price, vat_percent)
    return final_price

def calculate_order_summary(quantity, unit_price, unit_cost, discount_percent, vat_percent):
    initial_value = calculate_order_initial_value(quantity, unit_price)
    total_cost = calculate_total_cost(quantity, unit_cost)
    discounted_price = calculate_discounted_price(initial_value, discount_percent)
    discount_value = initial_value * discount_percent / 100
    vat_value = calculate_vat_value(discounted_price, vat_percent)
    final_price = discounted_price + vat_value
    profit = discounted_price - total_cost
    order_class = classify_order(final_price)
    profit_class = classify_profit(profit)
    discount_class = classify_discount(discount_percent)
    if discounted_price == 0:
       profit_margin = None
    else:
       profit_margin = calculate_profit_margin(discounted_price, total_cost)
    
    return {
        "initial_value": initial_value,
        "discount_percent": discount_percent,
        "discount_value": discount_value,
        "discounted_price": discounted_price,
        "vat_value": vat_value,
        "final_price": final_price,
        "total_cost": total_cost,
        "profit": profit,
        "order_class": order_class,
        "profit_class": profit_class,
        "discount_class": discount_class,
        "profit_margin": profit_margin
    }
    
def classify_order(final_price):        
    if final_price < 0:
        raise ValueError("Final price must be non-negative.")
    if final_price < 500:
        return "Small Order"
    elif 500 <= final_price <= 1000:
        return "Medium Order"
    else:
        return "Large Order"
    
def classify_discount(discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    if discount_percent == 0:
        return "No Discount"
    elif 0 < discount_percent <= 20:
        return "Standard Discount"
    else:
        return "High Discount"
    
def classify_profit(profit):
    if profit < 0:
        return "Loss"
    elif profit == 0:
        return "Break Even"
    else:
        return "Profit"
    

def calculate_total_cost(quantity, unit_cost):
    if quantity < 0 or unit_cost < 0:
        raise ValueError("Quantity and unit cost must be non-negative.")

    total_cost = quantity * unit_cost
    return total_cost