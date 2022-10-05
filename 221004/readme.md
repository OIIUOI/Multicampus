조건에 맞지 않는 input이 들어오면 바로 반려할 수는 없는가?

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = '__all__'

아티클 모델에 있는 모든 필드를 쓰겠다
이것은 기존의 폼을 대체할 수 있음
```
```python
# app/views.py

from .forms import ArticleForm

def new(request)
	article_form = ArticleForm()
	context = {
	'article_form' : article_form
	}
  return render(request, 'articles/new.html', context = context)

def create(request):
  # DB에 저장하는 로직
  article_form = articleForm(Request.POST)
  if article_form.is_valid():
    article_form.save()
  else:
    print('불충분한 입력')
    # 불충분한 입력이 있을 때 폼에 경고문이 뜸
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/new.html' context=context)
  return redirect('articles:index')
```