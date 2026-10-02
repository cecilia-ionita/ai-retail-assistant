import pandas as pd
from methods.sales import calculate_order_summary

def load_orders(file_path):
    orders_df = pd.read_csv(file_path)
    return orders_df

def get_order_by_id(orders_df, order_id):
    order = orders_df[orders_df["order_id"] == order_id]
    if order.empty:
        raise ValueError("Order ID not found.")
    return order

def process_order(order):
    summary = calculate_order_summary(
        order["quantity"],
        order["unit_price"],
        order["unit_cost"],
        order["discount_percent"],
        order["vat_percent"]
    ) 
    summary["order_id"] = order["order_id"]
    return summary

def process_all_orders(orders_df):
    summaries = []

    for row_index, order in orders_df.iterrows():
        summary = process_order(order)
        summaries.append(summary)
        
    return summaries



def calculate_total_sales(summaries):
    total_sales = 0

    for summary in summaries:
        total_sales += summary["final_price"]

    return total_sales    


def calculate_total_profit(summaries):
    total_profit = 0

    for summary in summaries:
        total_profit += summary["profit"]

    return total_profit  



def calculate_total_profit_margin(summaries):
    total_profit = calculate_total_profit(summaries)
    total_revenue = calculate_total_revenue(summaries)

    if total_revenue == 0:
        return None

    total_profit_margin = total_profit / total_revenue * 100
    return total_profit_margin


def calculate_total_orders(summaries):
    total_orders = len(summaries)    
    return total_orders 


def calculate_total_revenue(summaries):
    total_revenue = 0

    for summary in summaries:
        total_revenue += summary["discounted_price"]

    return total_revenue

def calculate_average_revenue_per_order(summaries):
    if len(summaries) == 0:
        return None

    total_revenue = calculate_total_revenue(summaries)
    total_orders = calculate_total_orders(summaries)

    return total_revenue / total_orders
    


def calculate_average_profit_per_order(summaries):
  
    if not summaries:
        return None

    total_profit = calculate_total_profit(summaries)
    total_orders = calculate_total_orders(summaries)

    return total_profit / total_orders


def calculate_average_discount_per_order(summaries):
    if not summaries:
        return None

    total_discount = calculate_total_discount_value(summaries)
    total_orders = calculate_total_orders(summaries)

    return total_discount / total_orders


def count_profitable_orders(summaries):
    count = 0
    for summary in summaries:
        if summary["profit"] > 0:
            count += 1
    return count

def count_loss_orders(summaries):
    count = 0
    for summary in summaries:
        if summary["profit"] < 0:
            count += 1
    return count

def count_break_even_orders(summaries):
    count = 0
    for summary in summaries:
        if summary["profit"] == 0:
            count += 1
    return count


def calculate_profitable_orders_percentage(summaries):
    if not summaries:
        return None

    profitable_orders = count_profitable_orders(summaries)
    total_orders = calculate_total_orders(summaries)

    return profitable_orders / total_orders * 100


def calculate_loss_orders_percentage(summaries):
    if not summaries:
       return None
     
    loss_orders = count_loss_orders(summaries)
    total_orders = calculate_total_orders(summaries)
     
    return loss_orders / total_orders * 100


def calculate_break_even_orders_percentage(summaries):
    if not summaries:
        return None
         
    break_orders = count_break_even_orders(summaries)
    total_orders = calculate_total_orders(summaries)
         
    return break_orders / total_orders * 100


def get_most_profitable_order(summaries):
    if not summaries:
        return None

    most_profitable_order = summaries[0]
    for summary in summaries:
        if summary["profit"] > most_profitable_order["profit"]:
            most_profitable_order = summary
    return most_profitable_order

def get_least_profitable_order(summaries):
    if not summaries:
            return None
    
    least_profitable_order = summaries[0]
    for summary in summaries:
            if summary["profit"] < least_profitable_order["profit"]:
                least_profitable_order = summary
    return least_profitable_order

def get_largest_order(summaries):
    if not summaries:
        return None

    largest_order = summaries[0]

    for summary in summaries:
        if summary["final_price"] > largest_order["final_price"]:
            largest_order = summary

    return largest_order
    
def get_smallest_order(summaries):
    if not summaries:
        return None

    smallest_order = summaries[0]

    for summary in summaries:
        if summary["final_price"] < smallest_order["final_price"]:
            smallest_order = summary

    return smallest_order


def calculate_business_summary(summaries):
    if not summaries:
        return None

    return {
       "total_revenue": calculate_total_revenue(summaries),
        "total_profit": calculate_total_profit(summaries),
        "profit_margin": calculate_total_profit_margin(summaries),
        "profitable_orders_percentage": calculate_profitable_orders_percentage(summaries),
        "loss_orders_percentage": calculate_loss_orders_percentage(summaries),
        "break_even_orders_percentage" : calculate_break_even_orders_percentage(summaries),
        "total_orders": calculate_total_orders(summaries),
        "average_revenue_per_order": calculate_average_revenue_per_order(summaries),
        "average_discount_value_per_order":calculate_average_discount_per_order(summaries),
        "average_profit_per_order": calculate_average_profit_per_order(summaries),
        "profitable_orders" : count_profitable_orders(summaries),
        "loss_orders": count_loss_orders(summaries),
        "break_even_orders" : count_break_even_orders(summaries),
        "largest_order" : get_largest_order(summaries),
        "smallest_order" : get_smallest_order(summaries),
        "total_customer_paid": calculate_total_sales(summaries),
        "total_discount_value" : calculate_total_discount_value(summaries),
        "average_customer_paid_per_order" : calculate_average_customer_paid_per_order(summaries),
       
    }
 
def calculate_total_discount_value(summaries):
    total_discount_value= 0

    for summary in summaries:
        total_discount_value += summary["discount_value"]

    return total_discount_value 


def calculate_average_customer_paid_per_order(summaries):
    if len(summaries) == 0:
        return None

    total_sales = calculate_total_sales(summaries)
    total_orders = calculate_total_orders(summaries)

    return total_sales / total_orders

    
       


