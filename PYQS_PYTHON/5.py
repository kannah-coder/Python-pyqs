
library_books = {
    "BookID": [101, 102, 103, 104, 105],
    "Title": ["Python 101", "Galactic Wars", "Data Structures", "Magic Lands", "AI for All"],
    "Author": ["John", "Alex", "Smith", "Laura", "Tina"],
    "Genre": ["Fiction", "Sci-Fi", "Fiction", "Fantasy", "Sci-Fi"],
    "TotalCopies": [10, 8, 6, 5, 7],
    "CopiesAvailable": [4, 2, 1, 3, 5]
}
# Dataset 6: Library Books
# 1. Write a Python program to calculate books issued = total - CopiesAvailable.
total_copies = 10 
copies_available = 4
books_issued = total_copies - copies_available
print("Books Issued:", books_issued)



# 2. Write a Python program using dictionary to count books per genre.
books = ["Fiction", "Sci-Fi", "Fiction", "Fantasy"]
from collections import Counter
genre_count = Counter(books)
print("Books per Genre:", genre_count)
# 3. Write a Python program to write/read to/from library.csv.
book_data = ["BookID,Title,Author,Genre,CopiesAvailable", "101,Python 101,John,Fiction,5"]
with open("library.csv", "w") as f:
    f.write("\n".join(book_data))
with open("library.csv", "r") as f:
    print(f.read())
# 4. Write a Python program using NumPy array of CopiesAvailable, apply mean and median.
import numpy as np
copies = np.array([3, 5, 2, 6, 4])
print("Mean:", np.mean(copies))
print("Median:", np.median(copies))

# 5. Write a Python program using Pandas to count books by Genre and sort.
import pandas as pd 
df = pd.DataFrame({
    'Genre': ['Fiction', 'Fantasy', 'Fiction', 'Sci-Fi']
})
print(df['Genre'].value_counts().sort_values(ascending=False))
# [Previous datasets unchanged]
