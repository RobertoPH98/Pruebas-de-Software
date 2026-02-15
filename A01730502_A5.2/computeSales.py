"""
This module computes the total sales from a price catalogue and sales records.
"""

import json
import sys
import time


def load_json_data(file_path):
    """
    Load data from a JSON file.
    Returns the data or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error reading file {file_path}: {error}")
        return None


def calculate_total_sales(catalogue, sales):
    """
    Calculate the total cost of sales based on the catalogue.
    """
    # Create a lookup dictionary for prices: {product_name: price}
    price_map = {item.get('title'): item.get('price') for item in catalogue}
    total_cost = 0.0

    for record in sales:
        product = record.get('Product')
        quantity = record.get('Quantity')

        if product in price_map and isinstance(quantity, (int, float)):
            total_cost += price_map[product] * quantity
        else:
            print(f"Invalid record or product not found: {record}")

    return total_cost


def main():
    """
    Main function to execute the program logic.
    """
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: python computeSales.py catalogue.json sales.json")
        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    catalogue_data = load_json_data(price_file)
    sales_data = load_json_data(sales_file)

    if catalogue_data is None or sales_data is None:
        sys.exit(1)

    total_cost = calculate_total_sales(catalogue_data, sales_data)
    elapsed_time = time.time() - start_time

    # Prepare output
    results = (
        f"--- Sales Report ---\n"
        f"Total Sales Cost: ${total_cost:,.2f}\n"
        f"Execution Time: {elapsed_time:.6f} seconds\n"
        f"--------------------"
    )

    # Print to console and save to file 
    print(results)
    with open("SalesResults.txt", "w", encoding='utf-8') as output_file:
        output_file.write(results)


if __name__ == "__main__":
    main()
    