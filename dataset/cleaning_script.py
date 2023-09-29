import pandas as pd
import os

def clean_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    
    # Drop duplicates
    data = data.drop_duplicates()
    
    # Drop rows with any missing values
    data = data.dropna()
    
    # Reset the index after dropping rows
    data = data.reset_index(drop=True)
    
    # Construct new file path for cleaned data
    dir_path, file_name = os.path.split(file_path)
    cleaned_file_name = f'cleaned_{file_name}'
    cleaned_file_path = os.path.join(dir_path, cleaned_file_name)
    
    # Save the cleaned data to a new file
    data.to_csv(cleaned_file_path, index=False)

# List of dataset files
files = [
    '/var/www/html/finance/dataset/customers_dataset.csv',
    '/var/www/html/finance/dataset/geolocation_dataset.csv',
    '/var/www/html/finance/dataset/order_items_dataset.csv',
    '/var/www/html/finance/dataset/order_payments_dataset.csv',
    '/var/www/html/finance/dataset/order_reviews_dataset.csv',
    '/var/www/html/finance/dataset/orders_dataset.csv',
    '/var/www/html/finance/dataset/product_category_name_translation.csv',
    '/var/www/html/finance/dataset/products_dataset.csv',
    '/var/www/html/finance/dataset/sellers_dataset.csv'
]

# Cleaning each file
for file in files:
    clean_data(file)
