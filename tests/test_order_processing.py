import pytest
from methods.order_processing import get_order_by_id, load_orders, process_order,process_all_orders,calculate_total_sales,calculate_total_profit,calculate_total_profit_margin,calculate_total_orders,calculate_average_profit_per_order, calculate_average_discount_per_order,count_profitable_orders,count_loss_orders,count_break_even_orders,calculate_profitable_orders_percentage,calculate_loss_orders_percentage,calculate_break_even_orders_percentage,get_most_profitable_order,get_least_profitable_order,get_largest_order,get_smallest_order,calculate_business_summary,calculate_total_revenue,calculate_total_discount_value,calculate_average_customer_paid_per_order


def test_load_orders():                    # verifică dimensiunea: 3 rânduri × 6 coloane
    orders_df = load_orders("data/orders.csv")
    assert orders_df.shape == (3, 6)
    
    
def test_load_orders_columns():            # verifică numele și ordinea coloanelor
    orders_df = load_orders("data/orders.csv")
    expected_columns = [
        "order_id",
        "quantity",
        "unit_price",
        "unit_cost",
        "discount_percent",
        "vat_percent",
    ]
    assert orders_df.columns.tolist() == expected_columns


@pytest.mark.parametrize(
    "column_name, expected_value",
    [
        ("order_id", "ORD001"),
        ("quantity", 3),
        ("unit_price", 200),
        ("unit_cost", 150),
        ("discount_percent", 10),
        ("vat_percent", 21),
    ],
)
def test_first_order_values(column_name, expected_value):
    orders_df = load_orders("data/orders.csv")
    assert orders_df.iloc[0][column_name] == expected_value
 
 
 
    
@pytest.mark.parametrize(
    "row_index, column_name, expected_value",
    [
        (0, "order_id", "ORD001"),
        (1, "quantity", 5),
        (2, "unit_cost", 120),
    ],
)
def test_order_values(row_index, column_name, expected_value):
    orders_df = load_orders("data/orders.csv")
    assert orders_df.iloc[row_index][column_name] == expected_value
    
    
def test_get_order_by_id():
    orders_df = load_orders("data/orders.csv")
    order = get_order_by_id(orders_df, "ORD002")
    assert order.shape == (1, 6)
    assert order.iloc[0]["order_id"] == "ORD002"
    
    
def test_get_order_by_id_not_found():
    orders_df = load_orders("data/orders.csv")

    with pytest.raises(ValueError):
         get_order_by_id(orders_df, "ORD999")

def test_process_order():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)

    assert summary["initial_value"] == 600
    
    
def test_process_order_discounted_price():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["discounted_price"] == 540
    
def test_process_vat_value_price():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["vat_value"] == 113.4
    
def test_process_final_price_price():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["final_price"] == 653.4
    
def test_process_total_cost():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["total_cost"] == 450
    
def test_process_profit():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["profit"] == 90
    

    
def test_process_profit_margin():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)

    assert summary["profit_margin"] == pytest.approx(16.6667, rel=1e-4)
    


def test_process_order_class():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["order_class"] == "Medium Order"
        
        
def test_process_profit_class():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["profit_class"] == "Profit"
        

def test_process_discount_class():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["discount_class"] == "Standard Discount"
    

def test_process_discount_value():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["discount_value"] == 60
    
def test_process_discount_percent():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["discount_percent"] == 10
    
def test_process_vat_percent():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[0]
    summary = process_order(order)
    assert summary["vat_percent"] == 21
    
def test_process_second_order():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[1]
    summary = process_order(order)
    assert summary["discount_class"] == "No Discount"
    assert summary["initial_value"] == 600
    assert summary["discount_value"] == 0
    assert summary["discounted_price"] == 600
    assert summary["vat_value"] == 126
    assert summary["final_price"] == 726
    assert summary["total_cost"] == 450
    assert summary["profit"] == 150
    assert summary["profit_margin"] == 25
    assert summary["order_class"] == "Medium Order"
    assert summary["profit_class"] == "Profit"
    assert summary["discount_percent"] == 0
    assert summary["vat_percent"] == 21
    
    
def test_process_third_order():
    orders_df = load_orders("data/orders.csv")
    order = orders_df.iloc[2]
    summary = process_order(order)
    assert summary["discount_class"] == "Standard Discount"
    assert summary["initial_value"] == 200
    assert summary["discount_value"] == 20
    assert summary["discounted_price"] == 180
    assert summary["vat_value"] == 37.8
    assert summary["final_price"] == 217.8
    assert summary["total_cost"] == 240
    assert summary["profit"] == - 60
    assert summary["profit_margin"] == pytest.approx(-33.3333, rel=3e-4)
    assert summary["order_class"] == "Small Order"
    assert summary["profit_class"] == "Loss"
    assert summary["discount_percent"] == 10
    assert summary["vat_percent"] == 21
     
     

def test_process_all_orders_structure():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
    assert len(summaries) == 3
    assert all(isinstance(summary, dict) for summary in summaries)
    assert summaries[0]["final_price"] == 653.4
    assert summaries[1]["profit"] == 150
    assert summaries[2]["profit_class"] == "Loss"
   
def test_calculate_total_sales():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    total_sales = calculate_total_sales(summaries)

    assert isinstance(total_sales, (int, float))
    assert total_sales == 1597.2
    
def test_calculate_total_profit():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
     
    total_profit = calculate_total_profit(summaries)
     
    assert isinstance(total_profit, (int, float))
    assert total_profit == 180
    
    
def test_calculate_total_revenue():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    total_revenue = calculate_total_revenue(summaries)

    assert isinstance(total_revenue, (int, float))
    assert total_revenue == 1320
    
    
def test_calculate_total_profit_margin():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    total_profit_margin = calculate_total_profit_margin(summaries)

    assert isinstance(total_profit_margin, (int, float))
    assert total_profit_margin == pytest.approx(13.6363, rel=3e-4)
    
    
def test_calculate_total_profit_margin_empty_list():
    summaries = []

    result = calculate_total_profit_margin(summaries)

    assert result is None 
    
def test_calculate_total_orders():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    total_orders = calculate_total_orders(summaries)

    assert total_orders == 3
    
    
def test_calculate_average_profit_per_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
        
    
    average_profit = calculate_average_profit_per_order(summaries)

    assert isinstance(average_profit, (int, float))
    assert average_profit  == 60
    
    
def test_calculate_average_profit_per_order_empty_list():
    summaries = []
    result = calculate_average_profit_per_order(summaries)
        
    assert result is None 
    
    
def test_calculate_average_discount_per_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    average_discount = calculate_average_discount_per_order(summaries)

    assert isinstance(average_discount, (int, float))
    assert average_discount == pytest.approx(26.6667, rel=1e-4)
    
    
def test_calculate_average_discount_per_order_empty_list():
    summaries = []
    result = calculate_average_discount_per_order(summaries)
        
    assert result is None 


    
def test_count_profitable_orders():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    profitable_orders = count_profitable_orders(summaries)

    assert isinstance(profitable_orders, int)
    assert profitable_orders == 2
    
    

def test_count_profitable_orders_empty_list():
    summaries = []
    result = count_profitable_orders(summaries)
            
    assert result == 0
    
    
    
def test_count_loss_orders():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
    
    loss_orders = count_loss_orders(summaries)
    
    assert isinstance(loss_orders, int)
    assert loss_orders == 1
        
    
    
def test_count_loss_orders_empty_list():
    summaries = []
    result = count_loss_orders(summaries)
                
    assert result == 0


def test_count_break_even_orders():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    assert count_break_even_orders(summaries) == 0
    
    
def test_count_break_even_orders_empty_list():
    summaries = []
    result = count_break_even_orders(summaries)
                    
    assert result == 0
   
def test_calculate_profitable_orders_percentage():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
    
    profitable_orders_percentage = calculate_profitable_orders_percentage(summaries)
    assert isinstance(profitable_orders_percentage, (int, float))
    assert profitable_orders_percentage == pytest.approx(66.6667, rel=1e-4)
    
    
def test_calculate_profitable_orders_percentage_empty_list():
    summaries = []
    result = calculate_profitable_orders_percentage(summaries)
                        
    assert result is None
    
def test_calculate_loss_orders_percentage():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
        
    loss_orders_percentage = calculate_loss_orders_percentage(summaries)
    assert isinstance(loss_orders_percentage, (int, float))
    assert loss_orders_percentage == pytest.approx(33.3333, rel=1e-4)  
    
    
def test_calculate_loss_orders_percentage_empty_list():
    summaries = []
    result = calculate_loss_orders_percentage(summaries)
                        
    assert result is None 


def test_calculate_break_even_orders_percentage(): 
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
        
    break_even_orders_percentage = calculate_break_even_orders_percentage(summaries)
    assert isinstance(break_even_orders_percentage, (int, float))
    assert break_even_orders_percentage == 0 
   
    
def test_calculate_break_even_orders_percentage_empty_list():
    summaries = []
    result = calculate_break_even_orders_percentage(summaries)
                        
    assert result is None 
    
def test_order_percentages_sum_to_100():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    profitable_order_percentage = calculate_profitable_orders_percentage(summaries)
    loss_order_percentage  = calculate_loss_orders_percentage(summaries)
    break_even_orders_percentage  = calculate_break_even_orders_percentage(summaries)
    
    assert profitable_order_percentage is not None
    assert loss_order_percentage is not None
    assert break_even_orders_percentage is not None
   
    total_percentage = (
        profitable_order_percentage 
        + loss_order_percentage  
        + break_even_orders_percentage
    )
    
    assert total_percentage == pytest.approx(100.0)
    
    
    
def test_get_most_profitable_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    result = get_most_profitable_order(summaries)
    assert result is not None
    assert isinstance(result, dict)
    assert result["order_id"] == "ORD002"
    assert result["profit"] == 150
    
    
    
def test_get_most_profitable_order_empty_list():
    summaries = []
    result = get_most_profitable_order(summaries)

    assert result is None
    
def test_get_least_profitable_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    result = get_least_profitable_order(summaries)

    assert result is not None
    assert isinstance(result, dict)
    # Verificăm că am identificat comanda cu cel mai mic profit
    assert result["order_id"] == "ORD003"
    assert result["profit"] == -60


def test_get_least_profitable_order_empty_list():
    summaries = []
    
    result =  get_least_profitable_order(summaries) 
    assert result is None
    
    
    
def test_get_largest_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    result = get_largest_order(summaries)
    assert result is not None
    assert isinstance(result, dict)
    assert result["final_price"] == 726
    assert result["profit"] == 150
    assert result["order_id"] == "ORD002"
    
    
    
    
def test_get_largest_order_empty_list():
    summaries = []
    result = get_largest_order(summaries)

    assert result is None
    
    
    
def test_get_smallest_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)


    result = get_smallest_order(summaries)
    print(result)

    assert result is not None
    assert isinstance(result, dict)
    assert result["final_price"] == 217.8
    assert result["profit"] == -60
    assert result["order_id"] == "ORD003"
   
    
    
def test_get_smallest_order_empty_list():
    summaries = []
    result = get_smallest_order(summaries)

    assert result is None
    
    
def test_calculate_business_summary():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    summary = calculate_business_summary(summaries)

    assert isinstance(summary, dict)
    assert summary["total_orders"] == 3
    assert summary["total_revenue"] == pytest.approx(1320.0)
    assert summary["total_profit"] == pytest.approx(180.0)
    assert summary["average_revenue_per_order"] == pytest.approx(440.0)  
    assert summary["profit_margin"] == pytest.approx(13.6363636364)    
    assert summary["profitable_orders_percentage"] == pytest.approx(66.6666666667)   
    assert summary["loss_orders_percentage"] == pytest.approx(33.33333333)   
    assert summary["break_even_orders_percentage"] == pytest.approx(0.0)  
    assert summary["average_discount_value_per_order"] ==  pytest.approx(26.6666666667)
    assert summary["average_profit_per_order"] == pytest.approx(60.0)    
    assert summary["profitable_orders"] ==  2        
    assert summary["loss_orders"] == 1 
    assert summary["break_even_orders"] == 0
    assert isinstance(summary["largest_order"], dict)
    assert summary["largest_order"]["order_id"] == "ORD002"
    assert summary["largest_order"]["final_price"] == pytest.approx(726.0)
    assert isinstance(summary["smallest_order"], dict)
    assert summary["smallest_order"]["order_id"] == "ORD003"
    assert summary["smallest_order"]["final_price"] == pytest.approx(217.8)
    assert summary["total_customer_paid"] == pytest.approx(1597.2)
    assert summary["total_discount_value"] == pytest.approx(80)
    



def test_calculate_business_summary_empty():
    summaries = []
    result =  calculate_business_summary(summaries)
    
    assert result is None


def test_calculate_total_discount_value_empty():
    summaries = []
    result = calculate_total_discount_value(summaries)
    
    assert result == 0
    
    
def test_calculate_total_discount_value():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    result = calculate_total_discount_value(summaries)

    assert result == pytest.approx(80)
    

def test_calculate_average_customer_paid_per_order():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)

    result = calculate_average_customer_paid_per_order(summaries)

    assert result == pytest.approx(532.4)  
    
    
def test_calculate_average_customer_paid_per_order_empty():
    summaries = []
    
    result = calculate_average_customer_paid_per_order(summaries)
    
    assert result is None
