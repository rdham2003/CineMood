import requests
import numpy as np
import pickle
import warnings
import pandas as pd
import os
import itertools
import datetime
import random
import time
import sqlite3
from flask import Flask, request, render_template
import subprocess

movieCount = 40

# os.system('cls')

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
    top3Genres = list(sortedGenreDict.keys())[:3]
    bottom3Genres = list(sortedGenreDict.keys())[::-1][:3]
    print(sortedGenreDict)
    print(top3Genres)
    print(bottom3Genres)
    
    genreTopSets = allPossibleSets(top3Genres)[::-1]
    print(genreTopSets)
    genreBottomSets = allPossibleSets(bottom3Genres)[::-1]
    print(genreBottomSets)
    print('\n')
    
    moviesToRecommend = []
    
    while (len(moviesToRecommend) < movieCount/2):
        for genre in genreTopSets:
            for movie in movieList:
                if (genre in movie[3]) and (movie not in moviesToRecommend):
                    moviesToRecommend.append(movie)
                if len(moviesToRecommend) == movieCount/2:
                    break
            if len(moviesToRecommend) == movieCount/2:
                    break
        if len(moviesToRecommend) == movieCount/2:
                    break   
    while (len(moviesToRecommend) < movieCount):
        for genre in genreBottomSets:
            for movie in movieList:
                if (genre in movie[3]) and (movie not in moviesToRecommend):
                    moviesToRecommend.append(movie)
                if len(moviesToRecommend) == movieCount:
                    break
            if len(moviesToRecommend) == movieCount:
                    break
        if len(moviesToRecommend) == movieCount:
                    break     
                  
    print(moviesToRecommend)
    print(len(moviesToRecommend))
    
    return moviesToRecommend

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/recommend', methods = ["GET", "POST"])
def recommendMovie():
    # randTime = random.randint(1,2)
    # for i in range(2):
    #     time.sleep(1)
    city = request.form.get("cityBox")
    state = request.form.get("stateBox")  # State code 
    country = request.form.get("countryBox")  # Country code 
    weatherAPI = '3f465ec287cfeb5fa02a21445f57f65b'

    weather_data = get_weather_by_city_state_country(city, country, weatherAPI, state)
    print(weather_data)
    try:
        weather_code = weather_data['weather'][0]['id']
    except KeyError:
        print("Error: Invalid location")
        return render_template("notvalid.html")

    if weather_code  == 762 or weather_code == 771 or weather_code == 781:
        print("Unstable weather conditions. Seek shelter immediately!")
        return render_template("unstable.html")

    current_time = "{:.2f}".format(np.round(((weather_data['dt']+weather_data['timezone']) % 86400) / 3600,2))
    dateTime = datetime.datetime.utcfromtimestamp(weather_data['dt']+weather_data['timezone'])

    model_input = np.array([weather_code, current_time]).reshape(1,-1)
    print(model_input)

    genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

    predict = weatherMovieModel.predict(model_input).tolist()[0]
    print(predict)
    # print(len(predict))
    # print(len(genres))

    predictedGenres = modelOutputToGenre(predict, genres)
    print(predictedGenres)

    with(open("VIP Files/TMDBmoviesData.csv", 'r')) as movieDB:
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
        dataList = [city, state, country, weather_data["weather"][0]["description"], dateTime.strftime("%I:%M %p"), modelOutput[randomMovie][1], modelOutput[randomMovie][2], modelOutput[randomMovie][3], modelOutput[randomMovie][4]]
        print(f'You live in {city}, {state}, {country}, where the current weather is {weather_data["weather"][0]["description"]} and the current time is {dateTime.strftime("%I:%M %p")}. Based on these conditions, I recommend you {modelOutput[randomMovie][1]}. {modelOutput[randomMovie][1]} is a {modelOutput[randomMovie][3]} genre movie and has a {modelOutput[randomMovie][2]} rating.')
        return render_template("recommend.html", data=dataList); 
    else:
        dataList = [city, country, weather_data["weather"][0]["description"], dateTime.strftime("%I:%M %p"), modelOutput[randomMovie][1], modelOutput[randomMovie][2], modelOutput[randomMovie][3], modelOutput[randomMovie][4]]
        print(f'You live in {city}, {country}, where the current weather is {weather_data["weather"][0]["description"]} and the current time is {dateTime.strftime("%I:%M %p")}. Based on these conditions, I recommend you {modelOutput[randomMovie][1]}. {modelOutput[randomMovie][1]} is a {modelOutput[randomMovie][3]} genre movie and has a {modelOutput[randomMovie][2]} rating.')
        return render_template("recommend.html", data=dataList);   
           
@app.route('/return', methods = ["POST"])
def goBack():
    return render_template("index.html")

@app.route('/metrics', methods = ["POST"])
def metrics():
    return render_template("modelMetrics.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)