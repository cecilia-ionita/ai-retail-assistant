def format_currency(value):
    return f"{value:,.2f}"


def generate_business_insights(summary):
    if not summary:
        return ["No order data available for analysis."]

    insights = [
        (
            f"Total revenue before VAT is {format_currency(summary['total_revenue'])}, "
            f"with total customer payments of {format_currency(summary['total_customer_paid'])}."
        ),
        (
            f"Total profit is {format_currency(summary['total_profit'])}, "
            f"with a profit margin of {summary['profit_margin']:.2f}%."
        ),
        (
            f"{summary['profitable_orders_percentage']:.2f}% of orders are profitable, "
            f"while {summary['loss_orders_percentage']:.2f}% generate a loss."
        ),
    ]

    largest_order = summary.get("largest_order")
    if largest_order:
        insights.append(
            f"The largest order is {largest_order['order_id']} with a final price of "
            f"{format_currency(largest_order['final_price'])}."
        )

    smallest_order = summary.get("smallest_order")
    if smallest_order:
        insights.append(
            f"The smallest order is {smallest_order['order_id']} with a final price of "
            f"{format_currency(smallest_order['final_price'])}."
        )

    return insights


def generate_recommendations(summary):
    if not summary:
        return ["Load order data before generating recommendations."]

    recommendations = []

    if summary["loss_orders"] > 0:
        recommendations.append(
            "Review loss-making orders and compare unit cost, discount level and final price."
        )

    if summary["profit_margin"] < 15:
        recommendations.append(
            "Profit margin is below 15%, so pricing, discounts and product costs should be reviewed."
        )

    if summary["average_discount_value_per_order"] > 0:
        recommendations.append(
            "Monitor discounts to ensure promotions support sales without reducing profitability too much."
        )

    if summary["profitable_orders_percentage"] >= 60:
        recommendations.append(
            "Most orders are profitable; identify what makes these orders perform well and replicate it."
        )

    if not recommendations:
        recommendations.append("Business performance is stable based on the current sample data.")

    return recommendations
