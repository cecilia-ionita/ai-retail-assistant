from methods.sales import calculate_sale_value, calculate_profit, calculate_profit_margin


def test_calculate_sale_value():
    result = calculate_sale_value(5, 120)
    assert result == 600


def test_calculate_profit():
    result = calculate_profit(600, 450)
    assert result == 150
    
    
def test_calculate_profit_margin():
    result = calculate_profit_margin(600, 450)
    assert result == 0.25   
    
