import pandas as pd
from math import sqrt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)

user_ratings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')#change matrix rows and columns

#remove movies which have less than 10 users who rated it
user_ratings = user_ratings.dropna(thresh=10,axis=1)
user_ratings = user_ratings.fillna(0)

item_similarity_df = user_ratings.corr(method="pearson")

def get_similar_movies(movie_name,user_rating):
	similar_score = item_similarity_df[movie_name]*(user_rating-2.5)
	similar_score = similar_score.sort_values(ascending=False)
	return similar_score
	
romantic_lover = [("Dracula: Dead and Loving It (1995)",5),("Money Train (1995)",5),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",0)]
similar_movies = pd.DataFrame()
for products,ratings in product_recom:
    similar_movies = similar_movies.append(get_similar_movies(products,ratings),ignore_index = True)

print("Recommended products according to user input are as follows:")
print(similar_movies.sum().sort_values(ascending=False).head(20))