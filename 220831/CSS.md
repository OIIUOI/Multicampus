## CSS Position

- 문서 상에서 요소의 위치를 지정

- static : 모든 태그의 기본 값(기준 위치)
  
  - 일반적인 요소의 배치 순서에 따름(좌측상단)
  
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  
  1. relative
  
  2. absolute
  
  3. fixed
  
  4. sticky
1. relative : 상대 위치
   
   - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
   
   - position: relative;

2. absolute
   
   - 요소를 문서 흐름에서 제거 (normal flow에서 벗어남)
   
   - position: absolute;

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-31-11-01-35-image.png)

## Flexbox

``display: flex;``

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

### 주축과 교차 축

- 주 축
  
  - `flex-direction: row;`   
    
    ``flex-direction: column;`` 

- 주축에 따라 item 정렬이 달라짐

### flex-wrap

- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정

- `flex-wrap:wrap;`
  
  ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-31-16-38-28-image.png)

- `flex-wrap: nowrap`
  
  ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-31-16-39-28-image.png)

### flex-direction

- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
  
  ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-31-16-29-56-image.png)

### flex-grow

[grow 설명](https://developer.mozilla.org/ko/docs/Web/CSS/flex-grow)

- flex-item 요소가 flex-container 내부에서 할당 가능한 **공간의 정도**를 선언

- `flex-grow: 3;` `flex-grow: 0.6`...

### flex-shrink

[shrink 설명]((https://developer.mozilla.org/ko/docs/Web/CSS/flex-shrink))

- flex-shrink 요소가 flex-container 크기보다 클 때 사용

### flex-basis

[basis 설명]((https://developer.mozilla.org/ko/docs/Web/CSS/flex-basis))

- 플렉스 아이템의 초기 크기를 지정

- default는 auto



body {

  margin: 0px

}


