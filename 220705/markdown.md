# 마크다운

> 텍스트 기반의 가벼운 마크업 언어
> 특수기호와 문자를 이용한 매우 간단한 문법을 사용하여 웹에서 빠르게 문서작업을 빠르게 할 수 있는 장점이 있어 읽고  쓰기에 편리해 많이 사용하는 언어이다

***



## Heading 헤딩
> 문서의 제목이나 소제목으로 사용

``` 
# 제목_1
## 제목_2
### 제목_3
#### 제목_4
##### 제목_5
###### 제목_6
```

# 제목_1
## 제목_2
### 제목_3
#### 제목_4
##### 제목_5
###### 제목_6

​		#의 갯수에 따라 구별되어지며, 

​		문서의 구조를 위해 작성되니 글자크기 조절을 위해서 사용하지는 말자

​		**유의해야 할 점은 # 뒤에 꼭 띄워쓰기를 해야지만 적용이 된다**



​		#이렇게 하면 제목으로 읽히지 않음

​		#제목_1 안읽히쥬?



## List 리스트

#### 순서가 있는 리스트

```
1. 을 입력하고 쓰고 싶은 목차를 입력하면 된다
Enter를 누르면 자연스럽게 2. 이 생기게 되고,
Tap 을 누르면 안으로 들여써지면서 목차 안의 목차가 생긴다

줄은 맞추면서 목차의 숫자는 없애고 싶을 때 ctrl + Enter를 누르면 된다
1.✔(띄워쓰고) 목차_1 로 입력해야 한다!
```



본인이 입력할 때에는 이렇게

```
1. 목차_1
목차_2
(tap) 목차_3
목차_4
(Ctrl + Enter) Ctrl + Enter 를 눌렀을 때의 모습
```



1. 목차_1

2. 목차_2

   1. 목차_3

   2. 목차_4

      ``Ctrl + Enter`` 를 눌렀을 때의 모습

이렇게 보여진다

참고로 2. 이라고 쓰면 2. 부터 시작하게 된다



---


#### 순서가 없는 리스트

```
- 리스트_1
- 리스트_2
- 리스트_3
```

간단히 앞에 -(하이픈)을 써주고 띄워써주고 내용을 적고 엔터치면 자연스럽게

이렇게 보인다



- 리스트_1

- 리스트_2

- 리스트_2

  Ctrl + Enter

  

마찬가지로 Ctrl + Enter 는 줄을 맞춰주면서 앞의 점을 없애준다





## 코드블럭 (Fenced Code Block)

코드를 메모장에 입력하면 정말 알아보기 힘든 경우가 많은데

간단하게 프로그램에 입력한 것처럼 보이게 해주는 문법이다

실제로 연산은 해주지 않는다



키보드 숫자 1 옆에 있는 물결무늬[ ~ ]를 보자

그 밑에 있는 ` 를 3번 누른 후 사용하고자 하는 언어를 입력,

코드를 입력해준 후 다시 ``` 를 누르면 된다



입력 :

``` pyt
``` python print(hello world)```
```



완성 :

```python
print(hello world)
```



print 가 파랗게 된 것처럼 if, for, while 등등도 색이 변하게 된다



## Inline code block (인라인 코드블럭)

메소드나 명령문 하나만 똑 떼서 한눈에 들어오게 보이게 하고 싶을 때 쓰면 좋다

`` 로 시작하고 안에 들어갈 문자 입력후 

다시 `` 를 써주면 된다



``` python
``split``
``if``
```



`` split`` 

``if``



## Link (하이퍼링크)

하이퍼링크 첨부법이다



```python
[문자](링크)

[네이버](www.naver.com)
[네이버] (www.naver.com)
```

[네이버](www.naver.com)

[네이버] (www.naver.com)



**띄워쓰기를 하면 하이퍼링크가 첨부되지 않으니 주의하자**



## 인용문

어떤 말을 인용할 때 쓰거나 정의를 쓰거나 할 때 유용하다

```python
```> 이것은 인용문```
```



> 이것은 인용문







## 표

``ctrl + T``  로 표 생성

|      |      |
| ---- | ---- |
|      |      |

한글파일 사용하듯이 만들어주는 게 속편하니 단축키를 기억하자





## Text 강조





|  ** 굵게 **  |  **굵게**  |
| :--: | :--------: |
| * 이탤릭체 *  |  *이탤릭*  |
| ~~  취소선 ~~ | ~~취소선~~ |

***과 문자열 사이에 띄워쓰기 없이 사용해야 기능이 발휘된다** 



## 수평선

내용의 단락을 나누고 싶을 때 사용하면 좋다



```pascal
***
---
___ (언더바 3개)
```



***

---

___



## 이미지

```pascal
![문자열](url)
![해바라기](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MDlfMjky%2FMDAxNjU0NzczOTYwODMy.N9f1aETnVNZrGCqFEJqdPg2WvTXgXbKq1As6grpDXJwg.HwqXH8ercYbGhdUTW2sSCiwBkXEKqVFJIOaZ21YanI8g.PNG.gnsdldmswjd%2FScreenshot_2022-06-09_at_20.19.18.png&type=sc960_832)
```



![해바라기](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MDlfMjky%2FMDAxNjU0NzczOTYwODMy.N9f1aETnVNZrGCqFEJqdPg2WvTXgXbKq1As6grpDXJwg.HwqXH8ercYbGhdUTW2sSCiwBkXEKqVFJIOaZ21YanI8g.PNG.gnsdldmswjd%2FScreenshot_2022-06-09_at_20.19.18.png&type=sc960_832)
