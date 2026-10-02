from methods.assistant import (
    format_currency,
    generate_business_insights,
    generate_recommendations,
)


def test_format_currency():
    assert format_currency(1597.2) == "1,597.20"


def test_generate_business_insights_empty_summary():
    assert generate_business_insights(None) == ["No order data available for analysis."]


def test_generate_recommendations_empty_summary():
    assert generate_recommendations(None) == [
        "Load order data before generating recommendations."
    ]


def test_generate_business_insights_with_summary():
    summary = {
        "total_revenue": 1320,
        "total_customer_paid": 1597.2,
        "total_profit": 180,
        "profit_margin": 13.6363,
        "profitable_orders_percentage": 66.6667,
        "loss_orders_percentage": 33.3333,
        "largest_order": {"order_id": "ORD002", "final_price": 726},
        "smallest_order": {"order_id": "ORD003", "final_price": 217.8},
    }

    insights = generate_business_insights(summary)

    assert len(insights) == 5
    assert "Total revenue before VAT is 1,320.00" in insights[0]
    assert "ORD002" in insights[3]
    assert "ORD003" in insights[4]


def test_generate_recommendations_with_summary():
    summary = {
        "loss_orders": 1,
        "profit_margin": 13.6363,
        "average_discount_value_per_order": 26.6667,
        "profitable_orders_percentage": 66.6667,
    }

    recommendations = generate_recommendations(summary)

    assert len(recommendations) == 4
    assert any("loss-making orders" in item for item in recommendations)
    assert any("Profit margin is below 15%" in item for item in recommendations)
