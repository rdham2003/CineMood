# CinemMood

**🎬About CineMood🎬**

CineMood is a free web application that utilizes a Machine Learning model to recommend a movie to the user based on their current location's date and time. This application collects weather information using the OpenWeatherAPI and returns a weather code and time. This code and time is then fed to a Machine Learning model and returns a list of genres. Next, this list is fed into an algorithm, which returns a list of 20 movies that best fit the given genres. Finally, a movie is randomly selected from this list and is recommended to the user. The user can freely swap through this list in case their first pick isn't to their liking.

**💡Inspiration💡**

Over the past month, I have been interested in 3 big topics: Machine Learning, AI, and Quant Trading. I wanted my career path to revolve around AI. My first step was to delve into 
the topic of Machine Learning. I had taken an online course on UDemy about ML and learned about numerous ML Algorithms such as Random Forest Classifier, Linear Regression, and K nearest neighbors. I wanted to create a project to exercise my knowledge. However, I wanted to create something new. Something that requires a dataset that cannot be found on Kaggle. During a discussion with friends, the topic of movies came up and what the best movies to watch during the rain were. That's when it hit me: I wanted to create an application that can easily give that. This app would not only recommend a movie for the rain, but also for any weather and the time of the day. I had already worked with OpenWeatherAPI while teaching myself about API calls and JSON, so it was also easier to gather ideas for this project.


**🛠️Tools Used🛠️**

**Languages**
* HTML
* CSS
* JavaScript
* Python
* SQL


**Libraries and Frameworks** 
* Numpy
* Pandas
* MatPlotLib
* Seaborn
* SciKit-Learn
* Flask

**Applied Topics** 
* Machine Learning
* API
* Front-end
* Back-end
* Full stack
* Database

**Machine Learning Model**: Multi-Label Random Forest Classifier

**📝Learning📝**

This project was not only built to help solve a confusion of what to watch based on weather and time conditions, but also to teach me about the vast world of Machine Learning.
This project helped me relearn many topics of statistics and discrete math and teach me many python libraries like SciKit-Lern, Pandas, and Seaborn. I also was able to learn how Machine Learning algorithms read data and return and output. This project also helped me in solidifying my knowledge in HTML, CSS, Javascript, Python, and SQL as well. 


**Repo Structure**

WeatherMovieApp2.0-main/
      .gitattributes      
      .gitignore
      ideas.txt
      README.md
      route.py
      Data/
          csvToSQL.py
          dataPreprocess.py
          generateData.py
          MovieDB.xlsx
          moviesInfo.db
          outputToCSV.py
      Model Training/
          ModelTraining.py
      static/
          main.css
          metrics.css
          movie.jpg
          Data Graphs/(21 graphs)
          moviePosters/(1000 poster images)
          fonts/
              FiraSansCondensed-Black.ttf
          js/
              loading.js
              results.js
              weather.js
      templates/
          index.html
          modelMetrics.html
          notvalid.html
          recommend.html
          unstable.html
      TestingPurposes/
          app.py
          setTheory.py
          test.py
          verifyPosterPath.py
      VIP Files/
          movieWeatherTimeData.csv
          movieWeatherTimeData2.csv
          TMDBmoviesData.csv
      weatherapp/
          Heebo-Bold.ttf
          weather.css
          weather.html
          weather.png
          weatherbackdrop.png
