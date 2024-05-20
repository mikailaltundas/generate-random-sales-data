import pandas as pd
import numpy as np
import random
from faker import Faker
import os
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the number of records per day
num_records = 1000

# Define product names and unit price ranges for each category
products_info = {
    'Electronics': [('Smartphone', (200, 1000)), ('Laptop', (500, 2000)), ('Headphones', (50, 300)), ('Camera', (100, 1500))],
    'Clothing': [('T-shirt', (10, 50)), ('Jeans', (20, 100)), ('Dress', (30, 200)), ('Sneakers', (50, 300))],
    'Home & Garden': [('Lamp', (20, 150)), ('Cushion', (5, 50)), ('Chair', (30, 200)), ('Blanket', (15, 100))],
    'Books': [('Novel', (10, 30)), ('Biography', (15, 40)), ('Science Fiction', (10, 30)), ('History', (20, 50))],
    'Health & Beauty': [('Shampoo', (5, 50)), ('Makeup Kit', (20, 100)), ('Perfume', (25, 200)), ('Skin Cream', (10, 75))],
    'Toys & Games': [('Board Game', (15, 60)), ('Action Figure', (10, 150)), ('Puzzle', (5, 50)), ('Video Game', (50, 60))]
}

# Create the directory if it does not exist
output_folder = 'clean_data'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Generate data for the last 10 days
start_date = datetime.now() - timedelta(days=9)
for single_date in (start_date + timedelta(n) for n in range(10)):
    # Create lists to store a day's data
    dates = []
    product_ids = []
    product_names = []
    categories = []
    unit_prices = []
    quantities_sold = []
    total_sales = []
    customer_ids = []
    payment_types = []
    first_names = []
    last_names = []

    # Generate fake data for a single day
    for _ in range(num_records):
        date = single_date.date()
        product_id = fake.unique.bothify(text='???-######')
        category = random.choice(list(products_info.keys()))
        product_choice = random.choice(products_info[category])
        product_name = product_choice[0]
        unit_price_range = product_choice[1]
        unit_price = round(random.uniform(*unit_price_range), 2)
        quantity_sold = random.randint(1, 9)
        total_sale = round(unit_price * quantity_sold, 2)
        customer_id = fake.unique.bothify(text='CUST-######')
        payment_type = random.choice(['Credit Card', 'Debit Card', 'Cash', 'Online Payment'])
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Append to lists
        dates.append(date)
        product_ids.append(product_id)
        product_names.append(product_name)
        categories.append(category)
        unit_prices.append(unit_price)
        quantities_sold.append(quantity_sold)
        total_sales.append(total_sale)
        customer_ids.append(customer_id)
        payment_types.append(payment_type)
        first_names.append(first_name)
        last_names.append(last_name)

    # Create a DataFrame for a single day
    sales_df = pd.DataFrame({
        'Date': dates,
        'Product_ID': product_ids,
        'Product_Name': product_names,
        'Category': categories,
        'Unit_Price': unit_prices,
        'Quantity_Sold': quantities_sold,
        'Total_Sales': total_sales,
        'Customer_ID': customer_ids,
        'First_Name': first_names,
        'Last_Name': last_names,
        'Payment_Type': payment_types
    })

    # Format date for filename
    formatted_date = single_date.strftime('%Y_%m_%d')
    csv_file_path = os.path.join(output_folder, f'{formatted_date}_Sales.csv')
    
    # Export to CSV
    sales_df.to_csv(csv_file_path, index=False)
    print(f"Data for {formatted_date} exported successfully to {csv_file_path}.")
