get_user_model 의 사용이유

user 모델의 변수화를 시켜주는 거임4

```python
from django.contrib.auth import get_user_model
# 이것의 뜻은

# setting.py
AUTH_USER_MODEL = 'accounts.User'

# 위의 것을 불러오는 것
```
