retail_sales_data_dict = {
    "ProductID": [1, 2, 3, 4, 5],
    "ProductName": ["Laptop", "T-Shirt", "Smartphone", "Shoes", "Headphones"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "QuantitySold": [10, 20, 15, 8, 12],
    "UnitPrice": [500, 30, 300, 100, 80]
}
# Dataset 3: Employee Attendance
# 1. Write a Python program to calculate attendance % = (DaysPresent / WorkingDays) * 100s
days_present = 20
working_days = 22
attendance_percent = (days_present / working_days) * 100
print("Attendance %:", attendance_percent)
#2
names = ["Alice", "Bob", "Alice", "Tom"]
unique_names = set(names)
print("Unique names:", unique_names)
#3
import csv
attendance_data = ["EmpID,Name,DaysPresent,WorkingDays", "101,John,20,22"]
with open("attendance.csv", "w", newline='') as f:
    f.write("\n".join(attendance_data))
with open("attendance.csv", "r") as f:
    print(f.read())

#4
import numpy as np
attendance_array = np.array([90, 80, 75, 95])
print("Above 80%:", attendance_array[attendance_array > 80])
print("Mean Attendance:", np.mean(attendance_array))

#5

# 5. Write a Python program using Pandas to calculate average DaysPresent by employee; filter absentees.
import pandas as pd
df = pd.DataFrame({
    'EmpID': [1,2,3],
    'Name': ['John', 'Alice', 'Tom'],
    'DaysPresent': [20, 18, 12]
})
print("Average Days Present:", df['DaysPresent'].mean())
print("Absentees (DaysPresent < 15):\n", df[df['DaysPresent'] < 15])
