# JavaScript

## 주석

- 한 줄 짜리 주석은 맨 앞에 이중 빗금(//)으로 작성

```javascript
// 나, 주석
```

- 여러 줄 주석은 /*과 */의 사이에 작성

```js
/*
 나 또한
 주석
*/
```

---

## let

값(숫자, 텍스트 문자열 등)에 이름을 붙이는 것

변수는 `let` 키워드와 그 뒤의 이름으로 생성할 수 있다

```js
let randomNumber = Math.floor(Math.random() * 100) + 1;
```

---

## const

상수 또한 변수처럼 이름을 붙인 값이지만 값은 바꿀 수 없다

상수는 `const` 키워드와 그 뒤의 이름으로 생성할 수 있다.

```js
const guesses = document.querySelector('.guesses');
```

---

## console

파이썬의 터미널 같은.. 느낌

- 기록 메서드

```js
console.log()
```

- 삭제 메서드

```js
console.clear()
```

---

## window

### `prompt()`

- 사용자로부터 문자열 입력을 받는 다이얼 로그 생성

- 입력받은 문자열을 반환해주어 코드에서 활용가능
  
  input() 같은..

```js
window.prompt('입력받을 때 할 안내문구')
```

### `alert()`

- 경고창

```js
window.alert('경고창에 쓸 안내문)## function
```

### `confirm()`

- 확인 취소 버튼이 있는 창을 띄움

```js
window.confirm('확인인지 취소인지 결정')
```

---

## function

- 함수 정의

```js
function checkGuess() {
 alert('I am a placeholder');
}
```

- 함수 콜

```js
checkGuess()
```

---

## 템플릿 리터럴

- 문자열 표현

```js
let number = 21
a = 12
console.log(
    'I like ${number} and ${a} too'
)

// I like 21 and 12 too
```

---

## null

- 없다를 의미하는 데이터

```js
let number;
// 이 변수에는 아무것도 없
number = null 
```

---

## undefined

- 데이터가 정의되지 않았다

```js
let number;
console.log(number)
// undefined
```

---

## boolean

- true, false 

- **True, False 는 안됨!!**

```js
let number;
number = true
number = false
```

`typeof` 

- 내가 사용하고 있는 데이터타입 확인

- 확인하고 싶은 데이터 앞에 붙이면 됨

---

## document

- `querySelector`

```js
// p 태그를 선택
document.querySelector('p')

// id가 text인 요소 선택
document.querySelector('#text')


// class가 text인 요소를 선택
document.querySelector('.text')
```

- `getElementById`

```js
// id가 text인 요소를 선택
document.getElementById('text')


// id가 image인 요소를 선택
document.getElementById('image')
```

- `textContent`

```js
// p 요소를 반환 받아 상수에 대입
const p = document.querySelector('p')


// p 요소의 textcontent 속성을 콘솔에 출력
console.log(p.textContent)


// p 요소의 textContent 값을 변경
p.textContent = '변경'
```

---

## 조건문 `if``else`

```js
/*
if (조건) {
    조건이 true 일 때 실행할 코
}
*/

let number = 3

if(number === 3) {
    console.log('it is true!')
}

/*
if (조건) {
    조건이 true 일 때 실행
}else{
    조건이 false 일 때 실행
}
*/


let number = 5
if (number == 3){
    console.log('it is true')
}else{
    console.log('it is false')
}
```

---

## 반복문

### `while`

```js
/*
while(조건){
    조건이 true인 동안에 반복 수행할 코드
}
*/


let number = 1
while(number < 3){
    console.log(number)
    number += 1
}
```

### `for`

```js
/*
for(초기식; 조건식; 반복식){
    조건이 true인 경우 반복 수행할 코드
}
*/

for(let i = 1; i <= 3; i += 1){
    console.log(i)
}
```
