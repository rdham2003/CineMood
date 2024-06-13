import requests
import numpy as np
import pickle
import warnings
import pandas as pd
import os
import itertools
import datetime
import random
from flask import Flask, request, render_template

os.system('cls')

app = Flask(__name__)

weatherMovieModel = pickle.load(open('model.pkl', 'rb'))
warnings.filterwarnings(action='ignore', category=UserWarning, message="X does not have valid feature names")

def get_weather_by_city_state_country(city, country, weatherAPI, state=None):
    if state:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={weatherAPI}'
        response = requests.get(url)
        return response.json()
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={weatherAPI}'
        response = requests.get(url)
        return response.json()
        

def modelOutputToGenre(predict, genres):
    predictedGenres = []
    for i in range(len(predict)):
        if predict[i] == 1:
            predictedGenres.append(genres[i])
    return predictedGenres

def allPossibleSets(lst):
    sets = []
    for i in lst:
        sets.append(i)
    for i in range(2,len(lst)+1):
        sets.extend(list(itertools.permutations(lst, i)))
    for i in range(len(sets)):
        if isinstance(sets[i], tuple):
            sets[i] = '|'.join(sets[i])
    return sets

def getBestMovies(movieList, genreList):
    genreDict = {}
    
    for i in genreList:
        genreDict[i] = 0
    
    keys = list(genreDict.keys())
    values = list(genreDict.values())
    
    for movie in movieList:
        for i in keys:
            if i in movie[3]:
                genreDict[i] += 1
    print(genreDict)
    
    sortedGenreDict = dict(sorted(genreDict.items(), key=lambda item: item[1], reverse=True))
    top3Genres = list(sortedGenreDict.keys())[:4]
    print(sortedGenreDict)
    print(top3Genres)
    
    genreSets = allPossibleSets(top3Genres)[::-1]
    print(genreSets)
    print('\n')
    
    moviesToRecommend = []
    
    while (len(moviesToRecommend) < 10):
        for genre in genreSets:
            for movie in movieList:
                if (genre in movie[3]) and (movie not in moviesToRecommend):
                    moviesToRecommend.append(movie)
                if len(moviesToRecommend) == 10:
                    break
            if len(moviesToRecommend) == 10:
                    break
        if len(moviesToRecommend) == 10:
                    break     
                  
    print(moviesToRecommend)
    print(len(moviesToRecommend))
    
    return moviesToRecommend


city = 'Eagan'
state = None  # State code 
country = 'US'  # Country code 
weatherAPI = '3f465ec287cfeb5fa02a21445f57f65b'

weather_data = get_weather_by_city_state_country(city, country, weatherAPI)
print(weather_data)
try:
    weather_code = weather_data['weather'][0]['id']
except KeyError:
    print("Error: Invalid location")
    exit()

if weather_code  == 762 or weather_code == 771 or weather_code == 781:
    print("Unstable weather conditions. Seek shelter immediately!")
    exit()

time = "{:.2f}".format(np.round(((weather_data['dt']+weather_data['timezone']) % 86400) / 3600,2))
dateTime = datetime.datetime.utcfromtimestamp(weather_data['dt']+weather_data['timezone'])

model_input = np.array([weather_code, time]).reshape(1,-1)
print(model_input)

genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

predict = weatherMovieModel.predict(model_input).tolist()[0]
print(predict)
# print(len(predict))
# print(len(genres))

predictedGenres = modelOutputToGenre(predict, genres)
print(predictedGenres)


with(open("VIP Files\TMDBmoviesData.csv", 'r')) as movieDB:
    movieData = movieDB.readlines()
    movieData = movieData[1:]
    movieDatabase = []
    for movie in movieData:
        movieLst = movie.split(',')
        movieLst[4] = movieLst[4][:-1]
        movieDatabase.append(movieLst)

# print(movieDatabase)

# allMovieSets = allPossibleSets(predictedGenres)
# print(allMovieSets)

recommendedMovies = []


for i in range(len(predictedGenres)):
    for movie in movieDatabase:
        genres = movie[3].split('|')
        if predictedGenres[i] in movie[3]:
            recommendedMovies.append(movie)

# print(recommendedMovies)

modelOutput = getBestMovies(recommendedMovies, predictedGenres)
randomMovie = random.randint(0,9)

print(modelOutput[randomMovie])
print("\n")

if state:
    print(f'You live in {city}, {state}, {country}, where the current weather is {weather_data["weather"][0]["description"]} and the current time is {dateTime.strftime("%I:%M %p")}. Based on these conditions, I recommend you {modelOutput[randomMovie][1]}. {modelOutput[randomMovie][1]} is a {modelOutput[randomMovie][3]} genre movie and has a {modelOutput[randomMovie][2]} rating.')
else:
    print(f'You live in {city}, {country}, where the current weather is {weather_data["weather"][0]["description"]} and the current time is {dateTime.strftime("%I:%M %p")}. Based on these conditions, I recommend you {modelOutput[randomMovie][1]}. {modelOutput[randomMovie][1]} is a {modelOutput[randomMovie][3]} genre movie and has a {modelOutput[randomMovie][2]} rating.')