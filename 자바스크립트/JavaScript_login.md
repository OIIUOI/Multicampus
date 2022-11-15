# Javascript

## Login

데이터 받아올 input 을 만들어주고 클릭했을 때의 이벤트 설정

```html
<body>
  <div id='login=form'>
    <input type="text" placeholder="name">
    <button>Log In</button>
  </div>
  <script>
    const loginForm = document.getElementById("login-form")
    const loginInput = loginform.querySelector("input")
    const loginButton = loginform.querySelector("button")

    // 위 3줄동일코드
    const loginInput = document.querySelector("#login-form input")
    const loginButton = document.querySelector("#login-form button")

    function onLoginButton() {
        console.log(loginInput.value); // value는 input의 입력값
      }
    loginbutton.addEventListener("click", onLoginButton);

  </script>
</body>
```

유효성 검사를 해보자

```html
<body>
  <div id='login-form'>
    <input type="text" placeholder="name">
    <button>Log In</button>
  </div>
  <script>
    const loginInput = document.querySelector("#login-form input")
    const loginButton = document.querySelector("#login-form button")

    function onLoginButton() {
        const username = login Input.value;
        if (username ==="") {
          alert("이름을 입력하셈")
        } else if(username.length > 15) {
          alert("이름 길이 너무 김")
        }
      }
    loginbutton.addEventListener("click", onLoginButton);

  </script>
</body>
```

근데 폼 쓰면 굳이 유효성검사하고 알람 설정하고 안 해도 됨 브라우저가 알아서 해줌

```html
<body>
 <form id='login-form'>
 <input required maxlength="15" type="text" placeholder="name">
 <button type="submit">Log In</button>
 </form> 
</body>
```

근데 submit 할 때마다 새로고침하기는 싫음

```html
<body>
 <form id='login-form'>
 <input required maxlength="15" type="text" placeholder="name">
 <button type="submit">Log In</button>
 </form> 

  <script>
    const loginInput = document.querySelector("#login-form input")
    const loginButton = document.querySelector("#login-form button")

    function onLoginSubmit(event) {
        event.preventDefault();
    }

    loginForm.addEventListener("submit", onLoginSubmit);

 </script>
</body>
```

submit을 할 때 onLoginSUbmit 함수를 실행시키는데 이 이벤트리스터가 정보도 같이 주면서 실행시키기 때문에 이 함수에 정보 받을 수 있게끔 입력값를 넣어준 거임

이 입력값에는 막 벌어진 일(=이벤트)에 대한 정보가 담겨있음

preventDefault 함수는 어떤 event의 기본행동이든지 발생하지 않도록 하는 것

> 기본 행동 = 어떤 함수에 대해 브라우저가 기본적으로 수행하는 동작
> 
> form 을 submit 하면 브라우저는페이지를 새로고침 하도록 되어 있음

annchor = a 태그

alert() 는 모든 기본행동을 막았다가 확인하면 기본동작을 수행

---

이제는 input에 입력한 값을 받아오고 싶음

```html
<head>
.hidden = {
  display: none;
}
</head>
<body>
 <form id='login-form'>
 <input required maxlength="15" type="text" placeholder="name">
 <button type="submit">Log In</button>
 </form> 
 <h1 id="greeting" class="hidden">aa</h1>
  <script>
    const loginForm = document.querySelector(".login-form");
    const greeting = document.querySelector("#greeting");
    const username = loginInput.value;

    function onLoginSubmit(event) {
        event.preventDefault();
        loginForm.classList.add("hidden");
        const username = loginInput.value;
        greeting.innerText= "hello " + username;
        greeting.classList.remove("hidden");
    }

    loginForm.addEventListener("submit", onLoginSubmit);

 </script>
</body
```

```javascript
// 아래 두 코드는 같은 코드다
greeting.innerText= "hello " + username;
greeting.innerText= `hello ${username}`;
```



받아온 username을 브라우저에 기억하게 하기 ( **localStorage** )

- `.removeItem`, `.getItem`, `.setItem`
  
  - localStorage 작은 DB 같은거임

```html
<head>
.hidden = {
  display: none;
}
</head><body>
 <form id='login-form'>
 <input required maxlength="15" type="text" placeholder="name">
 <button type="submit">Log In</button>
 </form> 
 <h1 id="greeting" class="hidden">aa</h1>
  <script>
    const loginForm = document.querySelector(".login-form");
    const greeting = document.querySelector("#greeting");
    

    function onLoginSubmit(event) {
        event.preventDefault();
        loginForm.classList.add("hidden");
        const username = loginInput.value;
        localSotrage.setItem("username",username)
        greeting.innerText= "hello " + username;
        greeting.classList.remove("hidden");
    }

    loginForm.addEventListener("submit", onLoginSubmit);

 </script>
</body
```



만약 예전에 username을 받아왔다면 로그인 폼이 보이지 않도록 해보자

```html
<head>
.hidden = {
  display: none;
}
</head><body>
 <form id='login-form'>
 <input required maxlength="15" type="text" placeholder="name">
 <button type="submit">Log In</button>
 </form> 
 <h1 id="greeting" class="hidden">aa</h1>
  <script>
    const loginForm = document.querySelector(".login-form");
    const greeting = document.querySelector("#greeting");
    
    const USERNAME_KEY = "username";

    function onLoginSubmit(event) {
        event.preventDefault();
        loginForm.classList.add("hidden");
        const username = loginInput.value;
        localSotrage.setItem(USERNAME_KEY,username)
        paintGreeting(username) 
    }
    
    function paintGreeting(username) {
      greeting.classList.remove("hidden");
      greeting.innerText = `Hello ${savedUsername}`;
    }

    const savedUsername = localStorage.getItem(USERNAME_KEY);

    if (savedUsername === null) {
      loginForm.classList.remove("hidden");
      loginForm.addEventListener("submit", onLoginSubmit);
    } else {
      paintGreeting(savedUsername) 
    }
 </script>
</body
```
