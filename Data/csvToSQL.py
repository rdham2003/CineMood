import sqlite3
import pandas as pd
import string

moviesDB = sqlite3.connect("moviesInfo.db")
moviesCursor = moviesDB.cursor()

def add_backslash(char):
    return f'\{char}'


createMovieDB = """CREATE TABLE IF NOT EXISTS MoviesInfo(
    movie_ID INTEGER,
    title VARCHAR(255),
    rating DOUBLE,
    genres VARCHAR(255),
    PosterFilePath TEXT
)"""

moviesCursor.execute(createMovieDB)

moviesCursor.execute("SELECT * FROM MoviesInfo")
movies = moviesCursor.fetchall()
print(len(movies))

if len(movies) == 0:
    with open("VIP Files\TMDBmoviesData.csv", 'r', encoding='utf-8') as file:
        movieList = file.readlines()
        movieDBList = movieList[1:]
        # print(print(movieDBList[6].split(',')))
        # print(len(movieDBList[6].split(',')))
        # test = movieDBList[6].split(',')
        # print(test[4][:-1])
        for movie in movieDBList:
            movieArray = movie.split(',')
            movieArray[4] = movieArray[4][:-1]
            print(movieArray)
            print(len(movieArray))
            query = "INSERT INTO MoviesInfo VALUES (?, ?, ?, ?, ?)"
            moviesCursor.execute(query, movieArray)
        print("Successfully created and filled Movie DB")   
    

for movie in movies:
    print(movie)
df = pd.read_sql_query("SELECT * FROM MoviesInfo", moviesDB)
df.to_excel('MovieDB.xlsx', index=False)
print("Created Movie Database Spreasheet")
