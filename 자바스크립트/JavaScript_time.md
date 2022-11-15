# JavaScript

## Interval

> 간격을 두고 자동으로 함수가 실행되게 하는 메서드

- `setInterval(함수, 초)`
  
  - 초에는 ms 이 들어감 1000ms = 1초

## TimeOut

> 웹페이지 실행 시 지정하는 초 후 함수가 실행되게 하는 메서드

- `setTimeout(함수, 초)`
  
  - 초에는 ms 이 들어감 1000ms = 1초

## Date

> 날짜표현

- `new date()`
  
  - 현재 지금의 날짜, 시간 표시
  
  | 메서드   date.~~  | 뭐하는지 |
  |:--------------:| ---- |
  | .getDate()     | 며칠인지 |
  | .getDay()      | 요일   |
  | .getFullYear() | 년도   |
  | .getHours()    | 몇 시  |
  | .getMinutes()  | 몇 분  |
  | .getSeconds()  | 몇 초  |

시계를 만들어보자

```html
<body>
  <h1 class="clock">00:00</h1>

  <script>
    const clock = document.querySelector(.clock);

    function getClock {
      const Date = new Date();
      clock.innerText(`${date.getHours()}:${date.getMinutes()}:`)
    }

    getClock(); // setInterval 때문에 바로 실행 안 되서 한번 실행시켜주는 거임
    setInterval(getClock, 1000);

  </script>
</body>
```

## pad

> 문자열에 패딩 넣기

- `.padStart(요구하는 문자열의 길이, "넣을 문자" )`
  
  - 문자열 앞부분에 문자 넣음

- `.padEnd(요구하는 문자열의 길이, "넣을 문자")`
  
  - 문자열 뒷부분에 문자 넣음

시계 표시형식을 좀 바꿔보자

```html
<body>
  <h1 class="clock">00:00</h1>

  <script>
    const clock = document.querySelector(.clock);

    function getClock {
      const Date = new Date();
      const date = new Date();  
      const hours = String(date.getHours()).padStart(2, "0");  
      const minutes = String(date.getMinutes()).padStart(2, "0");  
      const seconds = String(date.getSeconds()).padStart(2, "0");  
      clock.innerText =`${hours}:${minutes}:${seconds}`;
    }

    getClock(); // setInterval 때문에 바로 실행 안 되서 한번 실행시켜주는 거임
    setInterval(getClock, 1000);

  </script>
</body>
```
