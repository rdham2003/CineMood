const cityInput = document.getElementById("cityBox");
const stateInput = document.getElementById("stateBox");
const countryInput = document.getElementById("countryBox");
const weatherAPI = "3f465ec287cfeb5fa02a21445f57f65b";

document.getElementById("getWeather").addEventListener("submit", async function (event) {
    
    const city = cityInput.value;
    const state = stateInput.value;
    const country = countryInput.value;

    try{
        const weatherData = await getWeather(city,state,country);
        localStorage.setItem('weatherData', JSON.stringify(weatherData));
    }
    catch(error){
        console.error(error);
    }
});

async function getWeather(city, country, state = ""){
    let apiURL;
    if (state){
        apiURL = `https://api.openweathermap.org/data/2.5/weather?q=${city},${state},${country}&appid=${weatherAPI}`;
    }
    else{
        apiURL = `https://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${weatherAPI}`;
    }
    const response = await fetch(apiURL);
    // console.log(response);
    if (!response.ok){
        throw new Error("Could not fetch weather data")
    }
    return await response.json();
}



