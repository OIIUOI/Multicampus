# 장고

## static file

### 이미지

- **기본 세팅으로 되어있음**

```python
# setting.py

STATIC_URL = '/static/'
```

- app 폴더 안에 static 폴더 만들어서 
  
  그 안에 파일 위치

```html
<!-- app.html -->

{% block content %}

{% load static %}

<img src="{% static 'ff.jpg' %}>

{% endblock %}
```



static 폴더도 templates 처럼 관리되기 때문에 static 폴더 안에 앱이름으로 폴더를 한번 더 넣고 {% static '앱이름/그림파일이름' %} 하면 됨





### CSS  파일

- app 안에 css 폴더 만들어서 거기에 파일 넣으면 됨

```html
<!-- 메.html -->

<head>
    <link rel="stylesheet" href="{% static 'css/style.css'%}"
</head>
```



## 부트 스트랩

```bash
pip install django-bootstrap5
```

```python
# 앱등록
# settings.py

INSTALLED_APPS = {
    'django_bootstrap5',
}
```

  



TATP

아세톤 과산화수소수








