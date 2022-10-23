# django

## ◼ Static (템플릿에 파일 넣기 (이미지, CSS..))

### 앱단위로 static 폴더 관리할 때

app 안에 static 폴더 생성하고 이미지파일(filename.jpeg) 폴더에 넣기

```html
<!-- index.html 이미지를 넣을 html -->
{% load static %}


<img src="{% static 'filename.jpeg' %}">
```

settings 의 static 폴더로 관리하는데 안 건드려도 됨

static 폴더 안에 img 폴더, css 폴더로 나누어서 파일 관리를 한다면

```html
<!-- index.html 이미지를 넣을 html -->
{% load static %}

<img src="{% static 'img/filename.jpeg' %}">
```

css 파일을 불러올 때는

```html
{% load static %}

<head>
    <link rel="stylesheet" href="{% static 'ㅊㄴ/ㄴ쇼ㅣㄷ.ㅊㄴ%}"
</head>
```

### 프로젝트 단위로 static 폴더 관리할 때

```python
# settings.py

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

static 폴더 위치는 앱하위로 들어가지 않고 앱과 동등하게 있음

---

## ◼ 부트스트랩 설치

```bash
$ pip install bootstrap5
```

```python
# settings.py
app = [
    'bootstrap5',
]
```

윗부분은 인터넷에 찾아봐서 정확하게.. 

pip 부트스트랩 설치하고 앱에 부트스트랩 설치한 다음에

html 에 부트스트랩, css, javascript 을 로드해줌

```html
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
```

폼에서 부트스트랩 넣는 거는

```html
<form action=' method='POST'>
{% csrf_token %}
{% bootstrap_form 폼이름 %}
<input type='submit' value='완료'>
</form>
```

모델 폼 넣을 때랑 다른 거는  **{% bootstrap_form 폼이름 %}** 이거 밖에 없고 

다 똑같음

---

## ◼ r

## equest 에서 여러가지를 받음

- path
  
  ```html
  {% request.path %}
  <!-- articles/create -->
  ```

- url_name ( path 의 변수화)
  
  ```html
  {% request.resolver_match.url_name %}
  
  <!-- create -->
  ```

/8754210    **/resolver_match** request 를 풀어주는.. 번역해주는..

-*+*---## ◼ 표시형식 바꾸기

- Django Templates Filter (|~~~~) 

```html
<!-- 날짜형식 바꾸기 -->
{{ article.created_at|date:"y.m.d D" }}


<!-- ago filter 도 있다 -->
```

---

## ◼ admin

```bash
$ python manage.py createsuperuser
```

\]

.admin 에 모델 데이터베이스에 등록을 해야 admin 이 관리를 해줌

```python
# app/admin.py
from django.contrib import admin (# <- default)
from .models import ModelName

admin.site.register(ModelName)
```

---

## ◼ accounts

- 가입하기

```python
# accounts.models 모델 생성

from django.contrib.auth import AbstractUser # 인증과 대략의 폼이 생성되있음

class User(AbstractUser):
    pass

# settings

AUTH_USER_MODEL = 'accounts.User'

# accounts.forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserModel(UserCreationForm):
    class Meta:
        model = 'get_user_model()'
        fields = 'username'

# accounts.urls

app_name = 'accounts'
urlpatterns - [
    path('signup/', views.signup, name='signup')
]

# accounts.views
from .forms import CustomUserModel

def signup(request):
    if request.method == 'POST':
        userform = CustomUserModel(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('article:index')
    else:
        userform = CustomUserModel()
    context = ['userform' : userform]
    return render(request, 'accounts/signup.html', context)

# accounts.templates.accounts.signup

<form action="" method="post">
    {% csrf_token %}
    {{ userform }}
    <button ???= commit>가입</button>
</form>
```

---

- 로그인
  
  -  `AuthenticationForm` = 로그인 할 때 쓰는 폼
    
    - `AuthenticationForm`는 `django.contrib.auth.forms `에 위치
    
    - `AuthenticationForm` 는 form 을 상속받음
  
  - `login()` = 로그인 할 때 세션에 정보 등록 해주는 함수

```python
# accounts.urls

urlpatterns = [
    path('login', views.log_in, name = login)
]


# accounts.views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def log_in(request):
    if request.method == 'POST':
        loginform = AuthenticationForm(request, data = request.POST)
        if loginform.is_valid:
            login(request, loginform.get_user())
            return redirect('article:index')
    else:
        loginuser = AuthenticationForm()
    context = {'loginform' : loginuser}
    return render(request, 'accounts/login.html', context)


# accounts.templates.accounts.login.html
<form action="" method="post">
  {% csrf_token %}
  {{ loginform }}
  <button type="submit">login</button>
</form>
```

---

로그인이 무조건 필요하게끔

`@login_required`
