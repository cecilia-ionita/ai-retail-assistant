from methods.assistant import generate_business_insights, generate_recommendations
from methods.order_processing import (
    calculate_business_summary,
    load_orders,
    process_all_orders,
)


def main():
    orders_df = load_orders("data/orders.csv")
    summaries = process_all_orders(orders_df)
    business_summary = calculate_business_summary(summaries)

    print("AI Retail Assistant")
    print("===================")
    print()

    print("Business insights:")
    for insight in generate_business_insights(business_summary):
        print(f"- {insight}")

    print()
    print("Recommendations:")
    for recommendation in generate_recommendations(business_summary):
        print(f"- {recommendation}")


if __name__ == "__main__":
    main()
