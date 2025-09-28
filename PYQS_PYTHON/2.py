retail_sales_data= {
    "ProductID": [1, 2, 3, 4, 5],
    "ProductName": ["Laptop", "T-Shirt", "Smartphone", "Shoes", "Headphones"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "QuantitySold": [10, 20, 15, 8, 12],
    "UnitPrice": [500, 30, 300, 100, 80]
}

 # Dataset 2: Retail Sales Data
# 1. Write a Python program to calculate revenue = QuantitySold * UnitPrice.
quantity_sold = 10
unit_price = 50
revenue = quantity_sold * unit_price
print("Revenue:", revenue)
#2
sales = [("P1", 100), ("P2", 150), ("P3", 120)]
 
highest = max(sales,key=lambda x:x[1])
print("Product with highest sales:", highest)
##3
import json
sales_data = {"ProductID": 1, "ProductName": "ItemA", "Category": "Electronics", "QuantitySold": 20, "UnitPrice": 100}

with open("sales.json","w") as f:
    w1=json.dump(sales_data,f)
with open("sales.json","r") as f:
    print("after reading: ",json.load(f))  

# 4. Write a Python program using NumPy array of prices, apply max and sum.
import numpy as np
prices = np.array([100, 150, 200, 80])
print("Max price:", np.max(prices))
print("Total sum:", np.sum(prices))
#5
import pandas as pd
df = pd.DataFrame({
    'ProductID': [1, 2, 3],
    'Category': ['Electronics', 'Clothing', 'Electronics'],
    'QuantitySold': [10, 20, 15]
})
print(df.groupby('Category')['QuantitySold'].sum().sort_values(ascending=False))
