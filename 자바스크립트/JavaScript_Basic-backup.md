# JavaScript

## 기본 문법

### 기본함수

- alert("messege")
  
  - 알림창을 띄움
  
  - 확인을 요구
  
  - 받은 인자를 알창의 내용으로 사용

- prompt("messege", "answer")
  
  - 알림창을 띄움
  
  - 사용자의 입력을 요구
  
  - 첫번째 인자는 알림창의 메세지,
    
    두번째 인자는 디폴트 사용자의 입력으로 사용
    
    없을 경우

```javascript
const name = prompt("이름을 입력하세요.");
alert("환영합니다," + name + "님");
```

![](file://C:\Users\jin47\OneDrive\바탕 화면\multicampus\자바스크립트\assets\2022-10-30-12-36-15-image.png?msec=1668345907357)

- confirm
  
  - 확인받음

- const
  
  - 변하지 않는 상수 이름 지정

- let
  
  - 변하는 변수 이름 지정

- console.log()
  
  - 값을 콘솔창에 출력

- typeof **값**
  
  - 타입값 리턴
  
  - 괄호 X / 띄워쓴 후 값

- parseInt()
  
  - = int()

- isNaN()
  
  - number 인지 아닌지
  
  - 숫자가 아닐 때 true 리턴

### 데이터 타입

| 데이터타입     | 뜻            |
| --------- | ------------ |
| NaN       | 숫자가 아니다      |
| number    | 정수           |
| float     | 소수           |
| Booleans  | true / false |
| null      | ∅ / 공집합      |
| undefined | 정의된 변수가 없음   |
| string    | 문자열          |

#### array

```javascript
const myList = ['a', 'b', 'c', 'd'];
myList.push('e');


myList = ['a', 'b', 'c', 'd', 'e'];
myList[2] = 'f' 
//myList = ['a', 'b', 'f', 'd', 'e'];
```

#### objects

```javascript
const player = {
    name = 'fuckyou',
    hp = 100
};
console.log(player.name)
// fuckyou
console.log(player.hp)
// 100

player.hp = 150 => 값수정
player.mp = 50 => 값추가
```

### functions

```javascript
function sayhello(name) {
    console.log("hello " + name);
}

sayhello("fuckyou") 
// hello fuckyou

function plus(a,b) {
    return a+b;
}

const calculator = {
    plus : function (a, b) {
        return a + b;
    },
    minus : function (a, b) {
        return a - b;
}
};

console.log(calculator.minus(3,2))
// 1
console.log(calculator.plus(2,4))
// 6
```

### if 문

```javascript
if (// 조건){
    // 참일 경우
} else if (// 조건){
    // else if 에 해당하는 조
} else {
    // 거짓일 경우
}
```

- and = &&

- or = ||

## Javascript on the Browser

## select

- `getElementById("지정ID")`
  
  ```html
  <body>
  <h1 id="title">title</h1>
  <script>
  const title = document.getElementById("title");
  title.innerText = "a";
  </script>
  </body>
  
  =>
  a
  ```

- `getElementsByClassName("지정class")`
  
  ```html
  <body>
      <h1 class="a">AA</h1>
      <h1 class="a">AA</h1>
      <h1 class="a">AA</h1>
  <script>
  const hellos = document.getElementsByClassName("a");
  console.log(hellos.~~~);
  </script>
  </body>
  
  => 할수 없음 / array이기 때문
  ```

- `getElementsByTagName("지정태그")`
  
  > 태그는 h1, button, div 등등을 뜻함
  
  ```html
  <body>
     <h1 class="a">AA</h1>
     <h1 class="a">AA</h1>
     <h1 class="a">AA</h1>
  <script>
  const a = document.getElementsByTagName("h1");
  console.log(a.~~~);
  </script>
  </body>
  => 할 수 없음 / array이기 때문
  ```

- `querySelector`
  
  **.className innerTag**
  
  **#idName**
  
  ```html
  <body>
     <div class="a">
       <h1>AA</h1>
     </div>
  <script>const a = document.querySelector(".a h1");
  console.log(a);
  </script>
  </body>
  
  => AA
  
  <!-- 만약 h1 태그가 여러개라면?-->
  <body>
     <div class="a">
       <h1>AA</h1>
       <h1>BB</h1>
     </div>
  <script>
  const a = document.querySelector(".a h1");
  console.log(a);
  </script>
  </body>
  => AA
  <!-- 맨 처음 지정된 것이 선택-->
  
  <!-- 추가 -->
  
  <body>
    <div clas="a">
      <h1>AA</h1>
      <h1>BB</h1>
    </div>
    <script>
      const a = document.querySelector(".a:first-child h1");
      a.style.color = 'blue';
    </script>
  </body>
  ```

- `querySelectorAll`
  
  **.className innerTag** 쿼리를 모두 가져옴
  
  ```html
  <body>
     <div class="a">
       <h1>AA</h1>
       <h1>BB</h1>
     </div>
  <script>
  const a = document.querySelectorAll(".a h1");
  console.log(a);
  </script>
  </body>
  => array를 가져옴
  ```

### Event

```html
<body>
   <div class="a">
     <h1>AA</h1>
   </div>
<script>
const a = document.querySelector(".a h1");

function handleTitleClick() {
    console.log("a was clicked");
}

a.addEventListener("click", handleTitleClick);
a.onclick = handleTitleClick;
<!-- 위의 2줄 코드는 동일 -->
</script>
</body>
```
