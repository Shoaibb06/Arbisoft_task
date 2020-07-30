import pandas as pd
from matplotlib import pyplot as plt

# To draw a graph showing relation b/w rating count and rating score
def draw_rating_relation(data):
    plt.plot(data.rating_score, data.rating_count)
    plt.xlabel('Rating Score')
    plt.ylabel('Rating Count')
    plt.title('Relation between Rating Score and Rating Count')
    plt.show()

#to draw graph showing relation b/w rating score and budget
def draw_budget_rating_relation(data):
    plt.plot(data.rating_score, data.budget)
    plt.xlabel('Rating Score')
    plt.ylabel('Budget')
    plt.title('Relation between Rating Score and Budget')
    plt.show()

#to show average earning(Gross USA) of each genre in
def display_average_earning_by_genre(data):
    reshaped_data = (data.set_index(data.columns.drop('genre',2).tolist()) # as one movie can have multiple genres
       .genre.str.split(',', expand=True)                                # so duplicating the rows for movies
       .stack()                                                            # having more tha one genre
       .reset_index()
       .rename(columns={0:'genre'})
    )

    #grouping the data by each genre and cluclating its average earning and then sorting it in descending order
    average_earning_by_genre = reshaped_data.groupby('genre')['gross_usa'].mean().sort_values(ascending=False)
    print(average_earning_by_genre)

data = pd.read_csv('imdb_movies.csv')
data = data.sort_values('rating_score')

draw_rating_relation(data)
draw_budget_rating_relation(data)
display_average_earning_by_genre(data)

