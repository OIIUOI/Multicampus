# Django



## 가상환경 생성

```python
python -m venv [가상환경이름]
```



## 가상환경 실행

```python
# ls 명령어 입력 후 현재 경로에서 가상환경 폴더 확인


. [가상환경이름]/Scripts/actiave
```



## django LTS 버전 설치

```python
pip install django==3.2.13
```



## 앱 생성

```python
# ls 명령어 입력 후 현재 경로에서 manage.py 파일 확인
python manage.py startapp [앱이름]
```

## 앱 등록

```python
프로젝트설정폴더/settings.py - INSTALLED_APPS 리스트에 생성한 앱 추가
```



## 서버 실행

```python
python manage.py runserver
```






