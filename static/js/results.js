const card = document.getElementById("weatherCard");
const movieCard = document.getElementById("movie_container");

document.addEventListener('DOMContentLoaded', function() {
    const weatherData = JSON.parse(localStorage.getItem('weatherData'));
    if (weatherData){
        weatherInfo(weatherData);
    }
    else{
        document.getElementById("weatherCard").textContent = "No weather data found";
    }
    movieInfo(weatherData);
})

function weatherInfo(data){
    console.log(data);
    const name = data.name;
    const country = data.sys.country;
    const temp = data.main.temp;
    const temp_min = data.main.temp_min;
    const temp_max = data.main.temp_max;
    const windSpeed = data.wind.speed;
    const windDirection = data.wind.deg;
    const humidity = data.main.humidity;
    const feelsLike = data.main.feels_like;
    const weather = data.weather[0].main;
    const weatherID = data.weather[0].id;
    // console.log(name,temp, temp_min, temp_max, windSpeed, windDirection, humidity, feelsLike, weather, weatherID, country);
    const cityName = document.querySelector(".weatherCity");
    const cityTemp = document.querySelector(".temperature");
    const cityWeather = document.querySelector(".weatherReport");
    const cityEmoji = document.querySelector(".weatherEmoji");
    const cityFeelsLike = document.querySelector(".feelsLike");
    const cityHumidity = document.querySelector(".humidity");
    const cityWSpeed = document.querySelector(".windSpeed");
    const cityWdir = document.querySelector(".windDirection");
    cityName.textContent = `Current Weather at: ${movieData[0]}, ${movieData[1]}`;
    cityTemp.textContent = `${Math.round(((temp - 273.15) * (9/5) + 32))}° F`;
    cityWeather.textContent = weather;
    if (weatherID >= 200 && weatherID < 300) {
        cityEmoji.textContent = '⛈️';
        card.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(138, 177, 227))";
    } else if (weatherID >= 300 && weatherID < 400) {
        cityEmoji.textContent = '🌧️';
        card.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(138, 177, 227))";
    } else if (weatherID >= 500 && weatherID < 600) {
        cityEmoji.textContent = '🌧️';
        card.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(138, 177, 227))";
    } else if (weatherID >= 600 && weatherID < 700) {
        cityEmoji.textContent = '🌨️';
        card.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(255, 255, 255))";
    } else if (weatherID >= 700 && weatherID < 800) {
        cityEmoji.textContent = '🌫️';
        card.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(153, 152, 148))";
    } else if (weatherID >= 801 && weatherID < 900) {
        cityEmoji.textContent = '☁️';
        card.style.background = "linear-gradient(180deg, rgb(102, 101, 98), rgb(222, 221, 217))";
    } else if (weatherID == 800) {
        cityEmoji.textContent = '☀️';
        card.style.background = "linear-gradient(180deg, rgb(63, 162, 255),rgb(255, 174, 0))";
    }
    else {
        card.style.background = "default-background-style";
    }
    console.log(weatherID)
    cityFeelsLike.textContent = `Feels like: ${Math.round(((feelsLike - 273.15) * (9/5) + 32))}° F`;
    cityHumidity.textContent = `Humidity: ${humidity}%`;
    cityWSpeed.textContent = `Wind Speed: ${windSpeed}mph`;
    if (windDirection > 338 && windDirection <= 23){
        cityWdir.textContent = `Wind Direction: North`;
    }
    else if (windDirection > 23 && windDirection <= 68){
        cityWdir.textContent = `Wind Direction: Northeast`;
    }
    else if (windDirection > 68 && windDirection <= 113){
        cityWdir.textContent = `Wind Direction: East`;
    }
    else if (windDirection > 113 && windDirection <= 158){
        cityWdir.textContent = `Wind Direction: Southeast`;
    }
    else if (windDirection > 158 && windDirection <= 203){
        cityWdir.textContent = `Wind Direction: South`;
    }
    else if (windDirection > 203 && windDirection <= 248){
        cityWdir.textContent = `Wind Direction: Southwest`;
    }
    else if (windDirection > 248 && windDirection <= 293){
        cityWdir.textContent = `Wind Direction: West`;
    }
    else if (windDirection > 293 && windDirection <= 338){
        cityWdir.textContent = `Wind Direction: Northwest`;
    }
    console.log(windDirection);
    card.style.display = "block";
}

function movieInfo(data){
    const weatherID = data.weather[0].id;
    const movieTitle = document.getElementById("movieTitle");
    const rating = document.getElementById("rating");
    const genres = document.getElementById("genres");
    const moviePoster = document.getElementById("moviePoster");
    const currentWeather = document.getElementById("currentWeather");
    const currentTime = document.getElementById("currentTime");
    console.log('Movie Data:', movieData);
    if (weatherID >= 200 && weatherID < 300) {
        movieCard.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(138, 177, 227))";
    } else if (weatherID >= 300 && weatherID < 400) {
        movieCard.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(138, 177, 227))";
    } else if (weatherID >= 500 && weatherID < 600) {
        movieCard.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(138, 177, 227))";
    } else if (weatherID >= 600 && weatherID < 700) {
        movieCard.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(255, 255, 255))";
    } else if (weatherID >= 700 && weatherID < 800) {
        movieCard.style.background = "linear-gradient(180deg, rgb(79, 78, 77), rgb(153, 152, 148))";
    } else if (weatherID >= 801 && weatherID < 900) {
        movieCard.style.background = "linear-gradient(180deg, rgb(102, 101, 98), rgb(222, 221, 217))";
    } else if (weatherID == 800) {
        movieCard.style.background = "linear-gradient(180deg, rgb(63, 162, 255),rgb(255, 174, 0))";
    }
    else {
        movieCard.style.background = "default-background-style";
    }
    movieTitle.textContent = `${movieData[4]}`;
    rating.textContent = `${movieData[5]}⭐`;
    genres.textContent = `${movieData[6]}`;
    currentWeather.textContent = `Current Weather: ${movieData[2]}`;
    console.log(movieData[3][0]);
    if (movieData[3][0] == 0){
        currentTime.textContent = `Current Time: ${movieData[3].substr(1)}`
    }
    else{
        currentTime.textContent = `Current Time: ${movieData[3]}`;
    }

    // moviePoster.src = "{{ url_for('static', filename='moviePosters/') }}" + movieData[7];
    console.log(moviePoster.src);
}

function refresh(){
    location.reload();
}