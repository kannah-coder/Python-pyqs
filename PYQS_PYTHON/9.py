import pandas as pd
import numpy as np
 # Dataset 9: Movie Ratings
# 1. Write a Python program to calculate Weighted Rating = Rating * Votes.
rating = 4.5
votes = 2000
weighted_rating = rating * votes
print("Weighted Rating:", weighted_rating)

# 2. Write a Python program using dictionary to get top 3 genres.
genre_data = {"Action": 100, "Drama": 150, "Comedy": 90, "Thriller": 110}
top_genres = sorted(genre_data.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 Genres:", top_genres)

# 3. Write a Python program to write to/read from movies.csv.
movie_info = ["MovieID,Title,Genre,Rating,Votes", "1,Inception,Sci-Fi,4.8,2500"]
with open("movies.csv", "w") as f:
    f.write("\n".join(movie_info))
with open("movies.csv", "r") as f:
    print(f.read())

# 4. Write a Python program using NumPy to create rating array, apply sorting and average.
ratings = np.array([4.2, 3.8, 4.9, 4.5])
print("Sorted Ratings:", np.sort(ratings))
print("Average Rating:", np.mean(ratings))

# 5. Write a Python program using Pandas to group by Genre, average Rating and sort.
df = pd.DataFrame({
    'Genre': ['Action', 'Drama', 'Action', 'Drama'],
    'Rating': [4.2, 4.5, 4.0, 4.8]
})
print(df.groupby('Genre')['Rating'].mean().sort_values(ascending=False))
