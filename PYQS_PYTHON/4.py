weather_data= {
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Chennai"],
    "Date": ["2023-05-01", "2023-05-02", "2023-05-01", "2023-05-02", "2023-05-01"],
    "Temperature": [42, 40, 34, 33, 37],
    "Humidity": [60, 65, 70, 68, 75]
}
# Dataset 5: Weather Data
# 1. Write a Python program to convert Celsius to Fahrenheit.
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# 2. Write a Python program using list of temperatures, compute min and max.
temps = [30, 28, 35, 40, 32]
print("Min:", min(temps), "Max:", max(temps))

# 3. Write a Python program to save data to and read from weather.json.
import json
weather_data = {"City": "Delhi", "Date": "2023-05-01", "Temperature": 42, "Humidity": 60}
with open("weather.json", "w") as f:
    json.dump(weather_data, f)
with open("weather.json", "r") as f:
    print(json.load(f))

# 4. Write a Python program using NumPy to apply standard deviation and max on temperature.
import numpy as np
temp_array = np.array([30, 32, 35, 31, 33])
print("Std Dev:", np.std(temp_array))
print("Max Temp:", np.max(temp_array))

# 5. Write a Python program using Pandas to group by City, calculate average temperature and humidity.
import pandas as pd
df = pd.DataFrame({
    'City': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai'],
    'Temperature': [40, 42, 34, 33],
    'Humidity': [60, 65, 70, 68]
})
print(df.groupby("City")[['Temperature','Humidity']].mean())

