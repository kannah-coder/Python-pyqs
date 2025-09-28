import pandas as pd
import numpy as np
import json
inventory_data = {
    "ItemID": [1, 2, 3, 4],
    "Name": ["ItemA", "ItemB", "ItemC", "ItemD"],
    "Stock": [80, 120, 200, 50],
    "Price": [50, 30, 25, 100],
    "ExpiryDate": ["2025-12-31", "2026-05-01", "2023-12-31", "2024-06-30"]
}
# Dataset 10: Product Inventory
# 1. Write a Python program to calculate inventory value = Stock * Price.
stock = 50
price = 100
inventory_value = stock * price
print("Inventory Value:", inventory_value)

# 2. Write a Python program using list to store items, filter by Stock > 100.
items = [("ItemA", 80), ("ItemB", 120), ("ItemC", 200)]
high_stock = [item for item in items if item[1] > 100]
print("Items with stock > 100:", high_stock)

# 3. Write a Python program to write/read to/from inventory.json.
inventory = {"ItemID": 1, "Name": "ItemA", "Stock": 100, "Price": 50, "ExpiryDate": "2025-12-31"}
with open("inventory.json", "w") as f:
    json.dump(inventory, f)
with open("inventory.json", "r") as f:
    print(json.load(f))

# 4. Write a Python program using NumPy stock and price array to compute total value and variance.
stocks = np.array([50, 100, 80])
prices = np.array([20, 30, 25])
total_value = np.sum(stocks * prices)
print("Total Inventory Value:", total_value)
print("Stock Variance:", np.var(stocks))

# 5. Write a Python program using Pandas to filter expired products and compute stock per item.
df = pd.DataFrame({
    'ItemID': [1,2,3],
    'Stock': [50, 100, 80],
    'ExpiryDate': pd.to_datetime(['2024-01-01', '2026-05-01', '2023-12-31'])
})
today = pd.to_datetime('today')
print("Expired Products:\n", df[df['ExpiryDate'] < today])
print("Stock per Item:\n", df[['ItemID', 'Stock']])
