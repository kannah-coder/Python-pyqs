# common data set for five exercises
import pandas as pd
import numpy as np

# Common dataset used across all exercises
car_rental_data = {
    "CarID": [101, 102, 103, 104],
    "Brand": ["Toyota", "Ford", "Toyota", "BMW"],
    "DaysRented": [3, 7, 2, 5],
    "RatePerDay": [800, 1000, 850, 1200]
}
# Dataset 8: Car Rental Records
# 1. Write a Python program to calculate TotalRent = DaysRented * RatePerDay.
days = 5
rate = 1000
total_rent = days * rate
print("Total Rent:", total_rent)

# 2. Write a Python program using tuple list to calculate rent for each.
cars = [("CarA", 3, 500), ("CarB", 5, 1000)]
rents = [(c[0], c[1]*c[2]) for c in cars]
print("Car Rents:", rents)

# 3. Write a Python program to save and read rental.txt.
rental_info = "CarID: 101, Brand: Toyota, DaysRented: 4, RatePerDay: 900"
with open("rental.txt", "w") as f:
    f.write(rental_info)
with open("rental.txt", "r") as f:
    print(f.read())

# 4. Write a Python program using NumPy to calculate average and highest rent.
rents = np.array([3000, 4500, 6000, 7200])
print("Average Rent:", np.mean(rents))
print("Highest Rent:", np.max(rents))

# 5. Write a Python program using Pandas to calculate total rent per Brand and filter for high usage.
df = pd.DataFrame({
    'Brand': ['Toyota', 'Ford', 'Toyota', 'BMW'],
    'DaysRented': [3, 7, 2, 5],
    'RatePerDay': [800, 1000, 850, 1200]
})
df['TotalRent'] = df['DaysRented'] * df['RatePerDay']
 
print(df.groupby('Brand')['TotalRent'].sum())
print(df[df['DaysRented'] > 4])

