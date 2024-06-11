from PIL import Image
import os

def imgFound(file_path):
    return os.path.exists(file_path)

badMovies = []

imagesFound = 0
with(open("VIP Files\TMDBmoviesData.csv", "r")) as file:
    movieData = file.readlines()
    movieData = movieData[1:]
    for movie in movieData:
        movieLst = movie.split(',')
        movieLst[4] = movieLst[4][:-1]
        file_path = f'Data\moviePosters\{movieLst[4]}'
        print(f'{movieLst[3]}. Exists: {imgFound(file_path)}')
        if imgFound((f'Data\moviePosters\{movieLst[4]}')):
            imagesFound += 1
        else:
            badMovies.append(movieLst)
        # print(len(movieLst))
    print(f'Images Found: {imagesFound}')
    print(f'Images not found: {len(badMovies)}')
    print(badMovies)
    