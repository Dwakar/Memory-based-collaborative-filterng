import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

ratings = pd.read_csv('rating_final.csv')
cuisine= pd.read_csv('usercuisine.csv')

ratings = pd.merge(cuisine,ratings).drop(['placeID','food_rating','service_rating'],axis=1)
user_ratings = ratings.pivot_table(values='rating',index='userID',columns='Rcuisine')#change matrix rows and columns
user_ratings = user_ratings.dropna(thresh=10,axis=1)
user_ratings = user_ratings.fillna(0)

item_similarity_df = user_ratings.corr(method="pearson")
print(item_similarity_df)
def get_similar_cuisine(cuisine_name,user_rating):
	similar_score = item_similarity_df[cuisine_name]*(user_rating-2.5)
	similar_score = similar_score.sort_values(ascending=False)
	return similar_score

food_loved = [("American",5),("Mexican",1)]
similar_cuisine = pd.DataFrame()
for movie,rating in food_loved:
    similar_cuisine = similar_cuisine.append(get_similar_cuisine(movie,rating),ignore_index = True)

print("Recommended cuisine according to user input are as follows:")
print(similar_cuisine.sum().sort_values(ascending=False).head(20))
