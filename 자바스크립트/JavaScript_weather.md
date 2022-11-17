# JavaScript

날씨 할거임

위치값 받아서 날씨 api 주는 곳에서 api 키 받아오면 날씨랑 도시 보여줌

[Lecture – 노마드 코더 Nomad Coders](https://nomadcoders.co/javascript-for-beginners/lectures/2924)

openweathermap.org 가입해서 api 키 받아와야 함



Current Weather Data / API doc / By geographic coordinates / api call link



- `getCurrentPosition()`
  
  - 위치 받는 코드
  
  - 인자를 2개를 받음
    
    - 실행이 잘 됬을 때의 함수
    
    - 에러났을 때의 함수 
  
  - ```javascript
    function onGeoOk(position) {
        const lat = position.coords.latitud;
        const lng = position.coords.longitude;
        console.log(lat, lng);
    }
    
    function onGeoError() {
        alert("can't find you. Noweather for you.");
    }
    
    
    navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
    ```



```javascript
const API_KEY = "api 키 받아온 걸로 함"

function onGeoOk(position) {
    const lat = position.coords.latitud;
    const lng = position.coords.longitude;
    console.log(lat, lng);
    const url = "https://~~~"
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        const weather = document.querySelector("#weather span:first-child")
        const city =  document.querySelector("#weather span:last-child")
        city.innerText = data.name;
        weather.innerText = `${data.weather[0].main} / ${data.main.temp}`
    });
}

function onGeoError() {
    alert("can't find you. Noweather for you.");
}


navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
```
