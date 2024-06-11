import numpy as np
import pandas as pd
import datetime

samples = 10000

def movieWeatherGenre(code, time):
    genres = weatherToMovieDict[code]
    
    if code == 404 or code == 762 or code == 771 or code == 781:
        actionList.append(0)
        adventureList.append(0)
        animationList.append(0)
        childrenList.append(0)
        comedyList.append(0)
        crimeList.append(0)
        documentaryList.append(0)
        dramaList.append(0)
        fantasyList.append(0)
        historyList.append(0)
        horrorList.append(0)
        musicalList.append(0)
        mysteryList.append(0)
        romanceList.append(0)
        scifiList.append(0)
        thrillerList.append(0)
        warList.append(0)
        westernList.append(0)
        return
        
    if ("Action" in genres) or (time >= 12 and time < 18):
        actionList.append(1)
    else:
        actionList.append(0)
    if ("Adventure" in genres) or (time >= 6 and time < 12):
        adventureList.append(1)
    else:
        adventureList.append(0)
    if ("Animation" in genres) or (time >= 6 and time < 12):
        animationList.append(1)
    else:
        animationList.append(0)
    if ("Children" in genres) or (time >= 6 and time < 12):
        childrenList.append(1)
    else:
        childrenList.append(0)
    if ("Comedy" in genres) or (time >= 18 and time < 22):
        comedyList.append(1)
    else:
        comedyList.append(0)
    if ("Crime" in genres) or (time >= 18 and time < 22) or (time >= 22 or time < 6):
        crimeList.append(1)
    else:
        crimeList.append(0)
    if ("Documentary" in genres) or (time >= 18 and time < 22) or (time >= 22 or time < 6):
        documentaryList.append(1)
    else:
        documentaryList.append(0)
    if ("Drama" in genres) or (time >= 12 and time < 18):
        dramaList.append(1)
    else:
        dramaList.append(0)
    if ("Fantasy" in genres) or (time >= 6 and time < 18):
        fantasyList.append(1)
    else:
        fantasyList.append(0)
    if ("History" in genres) or (time >= 18 and time < 22) or (time >= 22 or time < 6):
        historyList.append(1)
    else:
        historyList.append(0)
    if ("Horror" in genres) or (time >= 22 or time < 6):
        horrorList.append(1)
    else:
        horrorList.append(0)
    if ("Musical" in genres) or (time >= 6 and time < 12):
        musicalList.append(1)
    else:
        musicalList.append(0)
    if ("Mystery" in genres) or (time >= 18 and time < 22) or (time >= 22 or time < 6):
        mysteryList.append(1)
    else:
        mysteryList.append(0)
    if ("Mystery" in genres) or (time >= 18 and time < 22):
        romanceList.append(1)
    else:
        romanceList.append(0)
    if ("Sci-Fi" in genres) or (time >= 22 or time < 6):
        scifiList.append(1)
    else:
        scifiList.append(0)
    if ("Thriller" in genres) or (time >= 22 or time < 6):
        thrillerList.append(1)
    else:
        thrillerList.append(0)
    if ("War" in genres) or (time >= 18 and time < 22):
        warList.append(1)
    else:
        warList.append(0)
    if ("Western" in genres) or (time >= 12 and time < 18):
        westernList.append(1)
    else:
        westernList.append(0)
        
weatherToMovieDict = {
        200: "Crime, Mystery, War",
        201: "Crime, Mystery, War",
        202: "Crime, Mystery, Thriller",
        210: "Crime, Mystery, Sci-Fi",
        211: "Crime, Documentary",
        212: "Horror, Thriller,Sci-Fi",
        221: "Horror, Thriller",
        230: "Crime, Thriller,Sci-Fi",
        231: "Crime, Thriller, Mystery",
        232: "Crime, Thriller, Mystery",
        300: "Romance, Documentry",
        301: "Romance, Documentry",
        302: "Romance, Documentry",
        310: "Romance, Documentry",
        311: "Romance, Documentry",
        312: "Romance, Documentry",
        313: "Romance, Documentry, History",
        314: "Romance, Documentry, History",
        321: "Romance, Documentry, History",
        404: "Not found",
        500: "History, Documentary",
        501: "History, Documentary",
        502: "History, Documentary, Crime, War",
        503: "History, Documentary, Crime, War",
        504: "History, Documentary, Crime, War",
        511: "History, Documentary, Crime, War",
        521: "History, Documentary, Crime, War",
        522: "History, Documentary, Crime, War",
        531: "Documentary, Crime, War",
        600: "Animation, Children, Adventure, Fantasy, Romance",
        601: "Animation, Children, Adventure, Fantasy, Romance",
        602: "Animation, Children, Adventure, Fantasy, Romance",
        611: "Animation, Children, Adventure, Fantasy, Romance",
        612: "Animation, Children, Adventure, Fantasy, Romance",
        613: "Animation, Children, Adventure, Fantasy, Romance",
        615: "Animation, Children, Adventure, Fantasy, Romance",
        616: "Animation, Children, Adventure, Fantasy, Romance",
        620: "Animation, Children, Adventure, Fantasy, Romance",
        621: "Animation, Children, Adventure, Fantasy, Romance",
        622: "Animation, Children, Adventure, Fantasy, Romance",
        701: "Western, Mystery, Crime",
        711: "Western, Mystery, Crime", 
        721: "Western, Mystery, Crime",
        731: "Western, Mystery, Crime",
        741: "Mystery, Crime",
        751: "Western, Mystery, Crime",
        761: "Western, Mystery, Crime",
        762: "Bro run dawg",
        771: "RUN",
        781: "Stop watching movies n run bro",
        800: "Action, Comedy, Fantasy",
        801: "Documentary, History",
        802: "Documentary, History",
        803: "Documentary, History",
        804: "Documentary, History",
    }



# movies_df = pd.read_csv("Data\moviesPrePro.csv")

# unique_genres = set()
# movies_df['genres'].str.split(',').apply(unique_genres.update)

# unique_genres = sorted(unique_genres)
# unique_genres = unique_genres[1:]
# print(unique_genres)
# print("\n")

unique_genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

keys = list(weatherToMovieDict.keys())
print(keys)
print("\n")

data = {
    'Movie Title': [],
    'Weather': np.random.choice(keys, size=samples),
    'Time': np.round(np.random.uniform(0.00,23.99, size=samples),2)
}
for i in unique_genres:
    data[i] = []

movieList = []
actionList = []
adventureList = []
animationList = []
childrenList = []
comedyList = []
crimeList = []
documentaryList = []
dramaList = []
fantasyList = []
historyList = []
horrorList = []
musicalList = []
mysteryList = []
romanceList = []
scifiList = []
thrillerList = []
warList = []
westernList = []
    
data["Movie Title"] = (movieList)

for i in range(samples):
    movieList.append(f'Movie {i+1}')
    movieWeatherGenre(data['Weather'][i], data['Time'][i])

data['Action'] = actionList
data['Adventure'] = adventureList
data['Animation'] = animationList
data['Children'] = childrenList
data['Comedy'] = comedyList
data['Crime'] = crimeList
data['Documentary'] = documentaryList
data['Drama'] = dramaList
data['Fantasy'] = fantasyList
data['History'] = historyList
data['Horror'] = horrorList
data['Musical'] = musicalList
data['Mystery'] = mysteryList
data['Romance'] = romanceList
data['Sci-Fi'] = scifiList
data['Thriller'] = thrillerList
data['War'] = warList
data['Western'] = westernList


print(data)
print("\n")



for i in data:
    print(len(data[i]))

movieDF = pd.DataFrame(data)
print(movieDF)
print("\n")

movieDF.to_csv('movieWeatherTimeData.csv', index=False)

print("CSV generated.")