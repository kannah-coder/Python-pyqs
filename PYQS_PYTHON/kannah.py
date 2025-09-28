# 5. Write a Python program using Pandas to count books by Genre and sort.
import pandas as pd
df = pd.DataFrame({
    'Genre': ['Fiction', 'Fantasy', 'Fiction', 'Sci-Fi']
})
print(df.value_counts().sort_values(ascending=False))

 