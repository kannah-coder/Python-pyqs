patients_data = {
    "PatientID": [1, 2, 3, 4, 5],
    "Name": ["Tom", "Alice", "Bob", "David", "Sara"],
    "Age": [55, 45, 72, 66, 30],
    "Disease": ["Flu", "Covid", "Flu", "Malaria", "Covid"],
    "Charges": [5000, 8000, 3000, 4000, 6000]
}
# Dataset 7: Hospital Patients
# 1. Write a Python program to apply 10% discount on Charges.
charges = 10000
discount = charges * 0.10
total = charges - discount
print("Total Charges after Discount:", total)

# 2. Write a Python program using list of dictionaries, extract patients above age 60.
d=[{"Name" : "kannah" ,"age":16},{"Name" : "vaibhav", "age":69},{"Name" : "ashwin", "age":96}]
senior=[p for p in d if p['age']>60 ]
print("senior: ",senior)


# 3. Write a Python program to write/read to/from patients.json.
import json
patient_data = {"PatientID": 1, "Name": "Tom", "Age": 55, "Disease": "Flu", "Charges": 5000}
with open("patients.json", "w") as f:
    json.dump(patient_data, f)
with open("patients.json", "r") as f:
    print(json.load(f))


# 4. Write a Python program using NumPy array of charges, apply filter and average.  
import numpy as np
charges_array = np.array([4000, 7000, 3000, 9000])
print("Above 5000:", charges_array[charges_array > 5000])
print("Average Charges:", np.mean(charges_array))
# 5. Write a Python program using Pandas to group by Disease, calculate total Charges and count.
import pandas as pd
df = pd.DataFrame({
    'Disease': ['Flu', 'Covid', 'Flu', 'Malaria'],
    'Charges': [2000, 8000, 3000, 4000]
})
print(df.groupby('Disease')['Charges'].agg(['sum', 'count']))
