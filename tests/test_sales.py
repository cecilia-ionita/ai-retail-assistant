import pytest

from methods.sales import calculate_discounted_price, calculate_final_price, calculate_order_initial_value, calculate_order_summary, calculate_price_with_vat, calculate_sale_value, calculate_profit, calculate_profit_margin, calculate_total_cost, calculate_vat_value, classify_discount, classify_order, classify_profit



def test_calculate_sale_value():
    result = calculate_sale_value(5, 120)
    assert result == 600


def test_calculate_sale_value_negative_unit_price():
    with pytest.raises(ValueError):
        calculate_sale_value(5, -120)
        
        
def test_calculate_profit():
    result = calculate_profit(600, 450)
    assert result == 150
    
    
    
def test_calculate_profit_negative_cost():
    with pytest.raises(ValueError):
        calculate_profit(600, -450)
        
def test_calculate_profit_negative_sale_value():
    with pytest.raises(ValueError):
        calculate_profit(-600, 450)   
     
     
def test_calculate_profit_loss():
    result = calculate_profit(600, 700)
    assert result == -100   
        
def test_calculate_profit_margin_zero_sale_value():
    with pytest.raises(ValueError):
        calculate_profit_margin(0, 450)
        
        
       
def test_calculate_profit_margin():
    result = calculate_profit_margin(600, 450)
    assert result == 25  
    
    
def test_calculate_sale_value_negative_quantity():
    with pytest.raises(ValueError):
        calculate_sale_value(-5, 120)
        
        
def test_calculate_profit_break_even():
    result = calculate_profit (600, 600)
    assert result == 0
    
    
def test_calculate_discounted_price():
    result = calculate_discounted_price(600, 10)
    assert result == 540
    
    
def test_calculate_discounted_price_negative_discount():
    with pytest.raises(ValueError):
        calculate_discounted_price(600, -10)
        
        
def test_calculate_discounted_price_over_100():
    with pytest.raises(ValueError):
        calculate_discounted_price(600, 110)
        
        
def test_calculate_discounted_price_zero_discount():
    result = calculate_discounted_price(600, 0)
    assert result == 600
    
    
def test_calculate_discounted_price_full_discount():
    result = calculate_discounted_price(600, 100)
    assert result == 0
 
 
def test_calculate_price_with_vat():
    result = calculate_price_with_vat(600, 21)
    assert result ==726
    
    
def test_calculate_price_with_vat_negative_vat():
    with pytest.raises(ValueError):
        calculate_price_with_vat(600, -21)
     
     
def test_calculate_price_with_vat_zero_vat():
    result = calculate_price_with_vat(600, 0)
    assert result == 600   
    
def test_calculate_price_with_vat_100_percent_vat():
    result = calculate_price_with_vat(600, 100)
    assert result == 1200
    
def test_calculate_price_with_vat_over_100():
    with pytest.raises(ValueError):
        calculate_price_with_vat(600, 110)
  
        
def test_calculate_final_price():
    sale_value = 600
    discount_percent = 10
    vat_percent = 21

    discounted_price = calculate_discounted_price(sale_value, discount_percent)
    final_price = calculate_price_with_vat(discounted_price, vat_percent)

    assert final_price == 653.4
    
    
def test_calculate_vat_value():
    result = calculate_vat_value(540, 21)
    assert result == 113.4
    
def test_calculate_zero_vat_value():
    result = calculate_vat_value(540, 0)
    assert result == 0
    
def test_calculate_vat_value_negative_vat():
    with pytest.raises(ValueError):
        calculate_vat_value(540, -21)
        
def test_calculate_vat_value_over_110():
    with pytest.raises(ValueError):
        calculate_vat_value(540, 110)
    
        
def test_calculate_vat_value_100_percent_vat():
    result = calculate_vat_value(540, 100)
    assert result == 540
    
def test_calculate_vat_value_zero_price():
    result = calculate_vat_value(0, 21)
    assert result == 0
    
def test_calculate_final_price_with_vat_and_discount():
    sale_value = 600
    discount_percent = 10
    vat_percent = 21
    discounted_price = calculate_discounted_price(sale_value, discount_percent)
    vat_value = calculate_vat_value(discounted_price, vat_percent)
    final_price = discounted_price + vat_value
    assert final_price == 653.4
    
    
def test_calculate_final_price_with_vat_and_discount_and_different_values():
    sale_value = 800
    discount_percent = 25
    vat_percent = 21
    discounted_price = calculate_discounted_price(sale_value, discount_percent)
    vat_value = calculate_vat_value(discounted_price, vat_percent)
    final_price = discounted_price + vat_value
    assert final_price == 726
    
def test_calculate_final_price_with_vat_and_discount_and_different_values2():
    sale_value = 1000
    discount_percent = 15
    vat_percent = 21
    discounted_price = calculate_discounted_price(sale_value, discount_percent)
    vat_value = calculate_vat_value(discounted_price, vat_percent)
    final_price = discounted_price + vat_value
    assert final_price == 1028.5
    
    
def test_calculate_order_initial_value():
    result = calculate_order_initial_value(3, 200)
    assert result == 600
    
    
def test_calculate_order_initial_value_negative_quantity():
    with pytest.raises(ValueError):
        calculate_order_initial_value(-3, 200)
        
def test_calculate_order_initial_value_negative_unit_price():
    with pytest.raises(ValueError):
        calculate_order_initial_value(3, -200)
        
def test_calculate_order_initial_value_zero_quantity():
    result = calculate_order_initial_value(0, 200)
    assert result == 0

def test_calculate_order_initial_value_zero_unit_price():
    result = calculate_order_initial_value(3, 0)
    assert result == 0
    
def test_calculate_final_price_value_negative_quantity():
    with pytest.raises(ValueError):
        calculate_final_price(-3, 200, 10, 21)

def test_calculate_final_price_value_negative_unit_price():
    with pytest.raises(ValueError):
        calculate_final_price(3, -200, 10, 21)

def test_calculate_final_price_value_negative_discount_percent():
    with pytest.raises(ValueError):
        calculate_final_price(3, 200, -10, 21)

def test_calculate_final_price_value_negative_vat_percent():
    with pytest.raises(ValueError):
        calculate_final_price(3, 200, 10, -21)
        
def test_calculate_final_price_value_discount_percent_over_100():
    with pytest.raises(ValueError):
        calculate_final_price(3, 200, 110, 21)
        
def test_calculate_final_price_value_vat_percent_over_100():
    with pytest.raises(ValueError):
        calculate_final_price(3, 200, 10, 110)
        
def test_calculate_final_price_value_discount_100():
    result = calculate_final_price(3, 200, 100, 21)
    assert result == 0
    
def test_calculate_final_price_value_vat_percent_100():
    result = calculate_final_price(3, 200, 10, 100)
    assert result == 1080
  
  
  
def assert_profit_data(result, total_cost, profit, profit_class, profit_margin):
    assert result["total_cost"] == total_cost
    assert result["profit"] == profit
    assert result["profit_class"] == profit_class

    if profit_margin is None:
        assert result["profit_margin"] is None
    else:
        assert result["profit_margin"] == pytest.approx(profit_margin, rel=1e-4)
        
        
          
def test_calculate_order_summary():
    result = calculate_order_summary(3, 200, 150, 10, 21)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 60
    assert result["discounted_price"] == 540
    assert result["vat_value"] == 113.4
    assert result["final_price"] == 653.4
    assert result["order_class"] == "Medium Order"
    assert result["discount_class"] == "Standard Discount"
    assert_profit_data(result, 450, 90, "Profit", 16.6667)
    
    
def test_calculate_order_summary_profit_loss():
    result = calculate_order_summary(3, 200, 200, 10, 21)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 60
    assert result["discounted_price"] == 540
    assert result["vat_value"] == 113.4
    assert result["final_price"] == 653.4
    assert result["order_class"] == "Medium Order"
    assert_profit_data(result, 600, -60, "Loss", -11.1111)

def test_calculate_order_summary_break_even():
    result = calculate_order_summary(3, 200, 180, 10, 21)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 60
    assert result["discounted_price"] == 540
    assert result["vat_value"] == 113.4
    assert result["final_price"] == 653.4
    assert result["order_class"] == "Medium Order"
    assert result["discount_class"] == "Standard Discount"
    assert_profit_data(result, 540, 0, "Break Even", 0)

def test_calculate_order_summary_no_discount():
    result = calculate_order_summary(3, 200,150, 0, 21)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 0
    assert result["discounted_price"] == 600
    assert result["vat_value"] == 126
    assert result["final_price"] == 726
    assert result["order_class"] == "Medium Order"
    assert_profit_data(result, 450, 150, "Profit", 25)

def test_calculate_order_summary_no_vat():
    result = calculate_order_summary(3, 200,150, 10, 0)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 60
    assert result["discounted_price"] == 540
    assert result["vat_value"] == 0
    assert result["final_price"] == 540
    assert result["discount_class"] == "Standard Discount"
    assert_profit_data(result, 450, 90, "Profit", 16.6667)
    

def test_calculate_order_summary_zero_quantity():
    result = calculate_order_summary(0, 200,150, 10, 21)
    assert result["initial_value"] == 0
    assert result["discount_value"] == 0
    assert result["discounted_price"] == 0
    assert result["vat_value"] == 0
    assert result["final_price"] == 0
    assert result["discount_class"] == "Standard Discount"
    assert result["profit_margin"] is None
    assert_profit_data(result, 0, 0, "Break Even", None)

def test_calculate_order_summary_zero_unit_price():
    result = calculate_order_summary(3, 0,150, 10, 21)
    assert result["initial_value"] == 0
    assert result["discount_value"] == 0
    assert result["discounted_price"] == 0
    assert result["vat_value"] == 0
    assert result["final_price"] == 0
    assert result["discount_class"] == "Standard Discount"
    assert result["profit_margin"] is None
    assert_profit_data(result, 450, -450, "Loss", None)
    
def test_calculate_order_summary_discount_percent_over_100():
    with pytest.raises(ValueError):
        calculate_order_summary(3, 200,150, 110, 21)
        
def test_calculate_order_summary_vat_percent_over_100():
    with pytest.raises(ValueError):
        calculate_order_summary(3, 200, 150,10, 110)
        
@pytest.mark.parametrize(
    "quantity, unit_price,unit_cost,discount_percent, vat_percent",
    [
        (-3, 200, 150, 10, 21),
        (3, -200, 150, 10, 21),
        (3, 200, -150, 10, 21),
        (3, 200, 150, -10, 21),
        (3, 200, 150, 10, -21),
    ]
)

def test_calculate_order_summary_invalid_inputs(quantity, unit_price,unit_cost,discount_percent, vat_percent):
    with pytest.raises(ValueError):
        calculate_order_summary(quantity, unit_price,unit_cost, discount_percent, vat_percent)
        
        
def test_calculate_order_summary_discount_100():
    result = calculate_order_summary(3, 200,150, 100, 21)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 600 
    assert result["discounted_price"] == 0
    assert result["vat_value"] == 0
    assert result["final_price"] == 0
    assert result["discount_class"] == "High Discount"
    assert_profit_data(result, 450, -450, "Loss", None)
          
def test_calculate_order_summary_vat_percent_100():
    result = calculate_order_summary(3, 200,150, 10, 100)
    assert result["initial_value"] == 600
    assert result["discount_value"] == 60 
    assert result["discounted_price"] == 540
    assert result["vat_value"] == 540
    assert result["final_price"] == 1080
    assert result["discount_class"] == "Standard Discount"
    assert_profit_data(result, 450, 90, "Profit", 16.6667)
    
def test_classify_order_negative():
    with pytest.raises(ValueError):
        classify_order(-1)
          
@pytest.mark.parametrize(
    "final_price, expected_result",
    [
        (499.99, "Small Order"),
        (500, "Medium Order"),
        (750, "Medium Order"),
        (1000, "Medium Order"),
        (1001, "Large Order"),
        (0, "Small Order"),
    ],
)
def test_classify_order(final_price, expected_result):
    result = classify_order(final_price)
    assert result == expected_result  

@pytest.mark.parametrize(
    "discount_percent, expected_result",
    [
        (0, "No Discount"),
        (0.01, "Standard Discount"),
        (20, "Standard Discount"),
        (20.01, "High Discount"),
        (100, "High Discount"),
    ]
)
def test_classify_discount(discount_percent, expected_result):
    result = classify_discount(discount_percent)
    assert result == expected_result
    
@pytest.mark.parametrize(
    "discount_percent",
    [
        -1,
        101,
    ]
)
def test_classify_discount_invalid(discount_percent):
    with pytest.raises(ValueError):
        classify_discount(discount_percent)
        
@pytest.mark.parametrize(
    "profit, expected_result",
    [
       (-150, "Loss"),
       (-0.01,"Loss"),
       (0, "Break Even"),
       (0.01, "Profit"),
       (150, "Profit"),
    ]
)
def test_classify_profit(profit, expected_result):
    result = classify_profit(profit)
    assert result == expected_result
    

    
@pytest.mark.parametrize(
    "quantity, unit_cost, expected_result",
    [
        (3, 150, 450),
        (0, 150, 0),
        (3, 0, 0),
        (2, 99.5, 199),
    ],
)
def test_calculate_total_cost(quantity, unit_cost, expected_result):
    result = calculate_total_cost(quantity, unit_cost)
    assert result == expected_result