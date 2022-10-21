# 장고



## admin

- 관리자사이트 아이디 및 비밀번호 만들기

```bash
# terminal

$ python manage.py createsuperuser
```

 

- 모델 등록
  
  ```python
  # admin.py
  
  from django.contrib import admin
  
  admin.site.register(Post)
  ```
