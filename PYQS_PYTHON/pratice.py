"""
retail_sales_data= {
    "ProductID": [1, 2, 3, 4, 5],
    "ProductName": ["Laptop", "T-Shirt", "Smartphone", "Shoes", "Headphones"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "QuantitySold": [10, 20, 15, 8, 12],
    "UnitPrice": [500, 30, 300, 100, 80]
}

rev=[q for q in retail_sales_data["QuantitySold"]]
u=[r for r in retail_sales_data['UnitPrice']]
a = [x * y for x, y in zip(rev, u)]
print("revenue: ",a)
"""
"""
online_orders_data_dict = {
    "OrderID": [201, 202, 203, 204, 205],
    "Customer": ["Alice", "Bob", "Alice", "Tom", "Bob"],
    "Date": ["2023-05-01", "2023-05-02", "2023-05-03", "2023-05-04", "2023-05-05"],
    "Item": ["Phone", "Laptop Bag", "Charger", "Tablet", "Headphones"],
    "Amount": [1000, 600, 300, 800, 150]
}
a=[0.18*a+a for a in online_orders_data_dict["Amount"]]
print("gst : ",a)
"""
"""
online_orders_data_dict = {
    "OrderID": [201, 202, 203, 204, 205],
    "Customer": ["Alice", "Bob", "Alice", "Tom", "Bob"],
    "Date": ["2023-05-01", "2023-05-02", "2023-05-03", "2023-05-04", "2023-05-05"],
    "Item": ["Phone", "Laptop Bag", "Charger", "Tablet", "Headphones"],
    "Amount": [1000, 600, 300, 800, 150]
}

a=[{h:r} for h,r in zip(online_orders_data_dict["Customer"],online_orders_data_dict["Amount"])]
print(a)
"""
library_books = {
    "BookID": [101, 102, 103, 104, 105],
    "Title": ["Python 101", "Galactic Wars", "Data Structures", "Magic Lands", "AI for All"],
    "Author": ["John", "Alex", "Smith", "Laura", "Tina"],
    "Genre": ["Fiction", "Sci-Fi", "Fiction", "Fantasy", "Sci-Fi"],
    "TotalCopies": [10, 8, 6, 5, 7],
    "CopiesAvailable": [4, 2, 1, 3, 5]
}

a=[a-b for a,b in zip(library_books["TotalCopies"],library_books['CopiesAvailable']) ]
print("the books issued: ",a)

from collections import Counter
print("counting: ",Counter(library_books["Genre"]))

# 5. Write a Python program using Pandas to count books by Genre and sort.
import pandas as pd
df = pd.DataFrame({
    'Genre': ['Fiction', 'Fantasy', 'Fiction', 'Sci-Fi']
})
print(df['Genre'].value_counts().sort_values(ascending=False))
    

 # 2. Write a Python program using tuple list to calculate rent for each.
cars = [("CarA", 3, 500), ("CarB", 5, 1000)]
rents = [(c[0], c[1]*c[2]) for c in cars]

# 2. Write a Python program using dictionary to get top 3 genres.
genre_data = {"Action": 100, "Drama": 150, "Comedy": 90, "Thriller": 110}
top_genres = sorted(genre_data.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 Genres:", top_genres)
