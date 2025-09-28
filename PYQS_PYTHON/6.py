online_orders_data_dict = {
    "OrderID": [201, 202, 203, 204, 205],
    "Customer": ["Alice", "Bob", "Alice", "Tom", "Bob"],
    "Date": ["2023-05-01", "2023-05-02", "2023-05-03", "2023-05-04", "2023-05-05"],
    "Item": ["Phone", "Laptop Bag", "Charger", "Tablet", "Headphones"],
    "Amount": [1000, 600, 300, 800, 150]
}# Dataset 4: Online Orders
# 1. Write a Python program to add 18% GST to each order amount.
amount = 1000
gst = amount * 0.18
total = amount + gst
print("Total with GST:", total)

# 2. Write a Python program using dictionary to store customer and list of amounts.
orders = {"Alice": [200, 300], "Bob": [150, 450]}
print("Customer Orders:", orders)

# 3. Write a Python program to write order details to orders.txt.
order_details = "OrderID: 201, Customer: Alice, Date: 2023-05-01, Item: Phone, Amount: 1000"
with open("orders.txt", "w") as f:
    f.write(order_details)
with open("orders.txt", "r") as f:
    print(f.read())

# 4. Write a Python program using NumPy to create array of order values, apply sum and percentile.
import numpy as np
order_values = np.array([400, 600, 1000, 300])
print("Total Sales:", np.sum(order_values))
print("90th Percentile:", np.percentile(order_values, 90))

# 5. Write a Python program using Pandas to group by Customer, compute total; filter orders > ₹500.
import pandas as pd
df = pd.DataFrame({
    'OrderID': [1,2,3,4],
    'Customer': ['Alice', 'Bob', 'Alice', 'Tom'],
    'Amount': [200, 600, 300, 800]
})
print(df.groupby("Customer")["Amount"].sum())
print(df[df["Amount"]>500])
