# django

## 이미지

- 필로우 라이브러리 설치
  
  ```bash
  pip install Pillow
  ```

- 모델에 이미지 필드 추가
  
  ```python
  # articles.models
  
  class Article(models.Model):
      ...
      ...
      image = models.ImageField(upload_to='images/', blacnk = True)
  ```

- 폼에 이미지 필드 추가
  
  ```python
  # articles.forms
  
  class ArticleForm(forms.Model)
      class Meta:
          model = Article
          fields = ['title, 'content', 'image']
  ```

- pjt.settings 에 미디어 설정 넣기
  
  ```python
  # settings
  
  MEDIA_ROOT = BASE_DIR / 'image'
  MEDIA_URL = '/media/'
  ```

- pjt.urls 에도 미디어 설정 넣기
  
  ```python
  ...
  ...
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      ...
      ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

- html form 에 이미지 파일 받을 수 있게끔 설정 추가 (enctype)
  
  ```html
  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ article_form }}
    <button type="submit">완료<ㅠ
  </form>
  ```

- 게시글 생성할 때 파일 받도록 views 수정
  
  ```python
  def create(request):
      if request.method == 'POST':
  #################################################################
          # request.FILES 를 추가로 받게됨
          article_form = ArticleForm(request.POST, request.FILES)
  #################################################################
          if article_form.is_valid(): 
              article.save()
              return redirect('articles:index')
      else: 
          article_form = ArticleForm()
      context = {
          'article_form': article_form
      }
      return render(request, 'articles/form.html', context=context)
  ```

- 게시글 detail.html 에 이미지 출력 코드 추가
  
  ```python
  {% if article.image %}
          <img src="{{ article.image.url }}" alt="" >
  {% endif % }
  ```

---

### 이미지 리사이징

- Django-imagekit 설치
  
  - 리사이징 할 때 쓰는 라이브러리
  
  ```bash
  $ pip install django-imagekit
  
  # setting
  INSTALLED_APPS = [
      ...
      'imagekit',
      ...
  ]
  ```
  
  - [자세한 모델 설정은 여기를 참조](https://github.com/matthewwithanm/django-imagekit)
  
  ```python
  # articles/models
  
  class Article(models.Model):
      ...
      image = ProcessedImageField(upload_to='images/', blank=True,
                                  processors=[ResizeToFill(1200, 960)],
                                  format='JPEG',
                                  options={'quality': 80})
  ```

---

### 이미지 업데이트

(사실 업데이트 아니고 덮어씌우기)

- views 에서 update 에서 request.FILES로 사진을 받아오게끔 설정
  
  ```python
  # views
  
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.user == article.user: 
          if request.method == 'POST':
   ###############################################################################3
               article_form = ArticleForm(request.POST, 
                              request.FILES, instance=article)
   ###########################################################################3
              if article_form.is_valid():
                   article_form.save()
                   return redirect('articles:detail', article.pk)
      else:
           article_form = ArticleForm(instance=article)
      context = {
      'article_form': article_form
      }
      return render(request, 'articles/form.html', context)
  ```

---

## 1:N 관계

> Article - Comment

### 댓글

- 댓글 모델 정의
  
  ```python
  # articles.models
  
  class Comment(models.Model):
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add = True)
   article = models.Foreignkey('Article' ,on_delete=models.CASCADE) 
  ```

- admin 에 등록하기
  
  ```python
  # admin
  from .models import Comment
  
  admin.site.register(Comment)
  ```

- 참조 역참조
  
  c 라는 중개테이블을 생성을 해주는 것, 근데 A에서 역참조 할 때 c_set 대신 d라는 이름으로 부르겠다
  
  ```python
  # models
  class A():
      ~~~
  
  class B():
      c = models.ManyToManyField('A', related_name = d)
  
  # 참조
  b.c.all()
  
  # 역참조
  a.d.all()
  
  # 데이터 저장 / 삭제
  b.c.add(a)
  b.c.remove(a)
  ```

- 댓글 폼 정의

```python
# forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
```

- 댓글 작성 폼 views 구현 (디테일 페이지에서 댓글작성)
  
  ```python
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      context = {
          'article': article,
          'comment_form': comment_form,
      }
      return render(request, 'articles/detail.html', context)
  ```

- detail.html 적용 (form url 처리 안하면 안됨?)
  
  ```html
  ...
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <button type="submit">OK</button>
  </form>
  ```

- 작성한 댓글을 저장하도록 url, views 구현

```python
# urls
path('int:pk/comments/', views.comment_create, 'name = comment_create')

# views

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
```

- 댓글 볼 수 있도록 detail.html 에 구현
  
  ```html
  {% for comment in comments %}
      <p> {{ comment.user.username }} | {{ comment.content }}</p>
      <hr>    
  {% empty %}
      <p>댓글이 없어요 ㅠ_ㅠ</p>
  {% endfor %}
  ```

---

## 1:N  ( User : Article )
