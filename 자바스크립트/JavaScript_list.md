# JavaScript

폼의 값을 받아서 리스트로 호출하는데 새로고침 하지 않게끔 하는 것이 목표다

우선 폼과  submit 이벤트 막기까지 했다

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈"
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input")
    const toDoList = document.getElementByID("todo-list");

    function handleToDoSUbmit(event) {
      event.preventDefault();
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);
  </script>
</body>
```

> 같은 코드

```javascript
const toDOInput = document.querySelector("#todo-form input")
const toDOInput = toDoForm.querySelector("input")
```

---

폼의 값은 받은 후에 폼을 비워줘야 함

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈"
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input")
    const toDoList = document.getElementByID("todo-list");

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);
  </script>
</body>
```

> 헷갈리는 것 (function handleToDoSubmit 에서의 2줄) 

```javascript
const newTodo = todoInput.value;
toDoInput.value = "";
```

첫번째 줄은 input의 현재 value를 새로운 변수에 **복사**하는 것임

복사한 다음에는 newTodo 와 toDoInput은 **아무 상관도 없음!!!** 

---

리스트로 호출하는 함수 만들자

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈" required>
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input")
    const toDoList = document.getElementByID("todo-list");


    function paintToDo(newTodo) {
      const li = document.createElement("li");
      const span = document.createElement("span");

      li.appendChild(span);
      span.innerText = newTodo;
      toDoList.appendChild(li);
    }

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";
      // 받은 toDoInput 값을 paintTodo 값에 보내주는 거임
      paintTodo(newTodo)
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);
  </script>
</body>
```

li 만들고 span 도 만듬 그리고 li 에 span 추가 해놓고 span.innerText 지정해준 다음에

toDoList 에 li를 추가해준 거임

---

근데 이건 삭제도 못함

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈" required>
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input")
    const toDoList = document.getElementByID("todo-list");

    function deleteToDo(event) {
      const li = event.target.parentElement;
      li.remove();
    }


    function paintToDo(newTodo) {
      const li = document.createElement("li");
      const span = document.createElement("span");
      const button = document.createElement("button");

      button.addEventListener("click", deleteToDo)

      li.appendChild(span);
      li.appendChild(button);
      span.innerText = newTodo;
      toDoList.appendChild(li);
    }

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";
      paintTodo(newTodo)
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);
  </script>
</body>
```

> 추가

```javascript
function deleteToDo(event) {
    const li = event.target.parentElement;
}
```

클릭으로 event 에 대한 정보를 받는데 

이것으로 클릭된 버튼의 부모를 찾아서 삭제를 해줘야 함 

근데 어떻게 접근을 할 것인가?

target 은 클릭된 HTML element 여기서는 클릭된 버튼을 말함

그리고 모든 HTML element 는 하나 이상의 property를 가지는데 

이것의 parentElement 는 클릭된 element의 부모임

이렇게 접근을 하게 된다

---

아 근데 새로고침 하면 없어지는데? 

localstorage 를 쓸꺼임

- `JSON.stringify()`
  
  - 자바스크립트의 값을 JSON 문자열로 변환
  
  - JSON 형식의 문자열로 변환된 데이터는 `.` 이나 `[]` 기호를 사용하여 접근 못함

- `JSON.parse()`
  
  - JSON 문자열을 JavaScript 객체로 변환
  
  - JavaScript 객체로 변환된 데이터는 `.`이나 `[]` 기호를 사용해서 접근 가능

- `forEach()`
  
  - for 문이랑 비슷하게 배열이 가지고 있는 요소들을 반복, for 문보다 빠르다
  
  - ```javascript
    배열명.forEach(요소명 => {
        실행문(요소명)
    });
    ```
  
  - ```javascript
    배열명.forEach(function(i) {
        console.log(i);
    });
    ```
  
  - ```javascript
    배열명.forEach(i => {
        console.log(i);
    });
    ```

- `for()`
  
  - ```javascript
    for (let i=0; i<배열명.length; i++ ) {
        console.log(i)
    }
    ```

- 화살표함수 `=>`
  
  - ```javascript
    let sum = (a, b) => a + b;
    
    /* 위 화살표 함수는 아래 함수의 축약 버전
    
    let sum = function(a, b) {
      return a + b;
    };
    */
    ```
    
    let sayHi = () => alert("hi")
    
    sayHi();
    
    ```
    
    ```

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈" required>
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input");
    const toDoList = document.getElementByID("todo-list");

    const toDos = [];
    const TODOS_KEY = "todos"

    function deleteToDo(event) {
      const li = event.target.parentElement;
      li.remove();
    }

    function saveToDos() {
      localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
    }

    function paintToDo(newTodo) {
      const li = document.createElement("li");
      const span = document.createElement("span");
      const button = document.createElement("button");

      button.addEventListener("click", deleteToDo)

      li.appendChild(span);
      li.appendChild(button);
      span.innerText = newTodo;
      toDoList.appendChild(li);
    }

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";
      toDos.push(newTodo);
      paintTodo(newTodo);
      saveToDos()
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);

    const savedToDos = localStorage.getItem(TODOS_KEY);

    if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    parsedToDos.forEach(element => console.log(item));
    }
  </script>
</body>
```

> 같은 코드

```javascript
function callList(item) {
    console.log(item);
};

if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    parsedToDos.forEach(callList);
};

// 위와 아래는 같다

if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    parsedToDos.forEach(item) => console.log(item));
};
```

---

근데 forEach에다가 input값 받아와서 써주는 함수 써주면 끝날듯?

그리고 todo 리스트가 localstorage에서 새로고침을 하고 새로운 todo를 추가하면 다 날아감

왜? `const toDos = []` 때문에!

toDos.push(newTodo) 는 빈 배열에 값을 넣기 때문임

그래서 toDos 배열을 let 으로 바꿔서 변경 가능하게 해주고

localStorage에 toDo 들이 있으면

`toDos = parsedToDos;` 를 추가해서 전에 있던 toDo를 복원함

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈" required>
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input");
    const toDoList = document.getElementByID("todo-list");

    let toDos = [];
    const TODOS_KEY = "todos"

    function deleteToDo(event) {
      const li = event.target.parentElement;
      li.remove();
    }

    function saveToDos() {
      localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
    }

    function paintToDo(newTodo) {
      const li = document.createElement("li");
      const span = document.createElement("span");
      const button = document.createElement("button");

      button.addEventListener("click", deleteToDo)

      li.appendChild(span);
      li.appendChild(button);
      span.innerText = newTodo;
      toDoList.appendChild(li);
    }

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";
      toDos.push(newTodo);
      paintTodo(newTodo);
      saveToDos()
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);

    const savedToDos = localStorage.getItem(TODOS_KEY);

    if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    toDos = parsedToDos;
    parsedToDos.forEach(paintToDo);
    }
  </script>
</body>
```

---

아 근데 toDo를 삭제하면 로컬스토리지에서도 삭제 되야 하는데 안되염;

id가 필요함 html에서는 구별하지만 toDos array 에서는 어떤 값을 삭제했는지 모름 

(동일한 문자열이 있다면 "a"가 2개라면 첫번째 "a"인지 두번째 "a"인지 모름)

그래서 이 toDos array에 딕셔너리로 [{id:1212, text:"a"}....] 이런 식으로 저장하고 싶음

이 id를 `Date.now()`로 구현 할거임 하면 (저장한 순간의 시간이 (년월일시분초ms) 나옴)

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈" required>
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input");
    const toDoList = document.getElementByID("todo-list");

    let toDos = [];
    const TODOS_KEY = "todos"

    function deleteToDo(event) {
      const li = event.target.parentElement;
      li.remove();
    }

    function saveToDos() {
      localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
    }

    function paintToDo(newTodo) {
      const li = document.createElement("li");
////////////////////////////////////////
      li.id = newTodo.id;
////////////////////////////////////////
      const span = document.createElement("span");
      const button = document.createElement("button");

      button.addEventListener("click", deleteToDo)

      li.appendChild(span);
      li.appendChild(button);
////////////////////////////////////////
      span.innerText = newTodo.text;
////////////////////////////////////////
      toDoList.appendChild(li);
    }

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";

//////////////////////////////////////
      const newTodoObj = {
        id : Date.now(),
        text : newTodo
      }
      toDos.push(newTodoObj);
      paintTodo(newTodObj);
      saveToDos()
///////////////////////////////////////
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);

    const savedToDos = localStorage.getItem(TODOS_KEY);

    if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    toDos = parsedToDos;
    parsedToDos.forEach(paintToDo);
    }
  </script>
</body>
```

---

아직 삭제하는 건 안했음

삭제하는 건 어떻게 할거냐면 `filter()` 라는 걸 쓸꺼임

- `filter()`
  
  - 특정 조건을 만족하는 새로운 배열을 필요로 할 때 사용
  
  - `배열.filter(함수 or 조건);`
  
  - ```javascript
    const arr = [1,2,3,4,5].filter(return true);
    console.log(arr);
        // [1,2,3,4,5]
    
    const arr_1 = [1,2,3,4].filter(number => number > 2);
    console.log(arr_1);
        // [3,4]
    ```

```html
<body>
  <form id="todo-form">
    <input type="text" placeholder="할일을 적으셈" required>
  </form>

  <ul id=""></ul>

  <script>
    const toDoForm = document.getElementById("todo-form");
    const toDOInput = toDoForm.querySelector("input");
    const toDoList = document.getElementByID("todo-list");

    let toDos = [];
    const TODOS_KEY = "todos"

    function deleteToDo(event) {
      const li = event.target.parentElement;
//////////////////////////////////////
      // li.remove(); => 삭제
      toDos = toDos.filter(todo => toDo.id !== parseInt(li.id));
//////////////////////////////////////
    }

    function saveToDos() {
      localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
    }

    function paintToDo(newTodo) {
      const li = document.createElement("li");
      li.id = newTodo.id;
      const span = document.createElement("span");
      const button = document.createElement("button");

      button.addEventListener("click", deleteToDo)

      li.appendChild(span);
      li.appendChild(button);
      span.innerText = newTodo.text;
      toDoList.appendChild(li);
    }

    function handleToDoSubmit(event) {
      event.preventDefault();
      const newTodo = todoInput.value;
      toDoInput.value = "";

      const newTodoObj = {
        id : Date.now(),
        text : newTodo
      }
      toDos.push(newTodoObj);
      paintTodo(newTodObj);
      saveToDos()
    }

    toDoForm.addEventListener("submit", handleToDoSubmit);

    const savedToDos = localStorage.getItem(TODOS_KEY);

    if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    toDos = parsedToDos;
    parsedToDos.forEach(paintToDo);
    }
  </script>
</body>
```
