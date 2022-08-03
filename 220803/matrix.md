# 이차원 리스트

> 세상에 있는 데이터를 표현하는 방식 (행렬)

## 

## 이차원 리스트

> 이차원 리스트는 행렬(matrix)이다
> 
> 리스트를 원소로 가진다  

| ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-03-10-27-46-image.png) | ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-03-10-28-10-image.png) |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |

- 특정 값으로 초기화 된 이차원 리스트 만들기
  
  1. 직접 작성(4x3 행렬)
     
     ```python
     matrix = [[0,0,0],[0,0,0],[0,0,0]]
     ```
  
  2. 반복문으로 작성 (n * m 행렬)
     
     ```python
     n = 4
     m = 3
     matrix = []
     
     for _ in range(n):
        matrix.append([0]*m)
     pprint(matrix)
     >>> [[0,0,0
        [0,0,0],
        [0,0,0]
        [0,0,0]]
     
     = matrix_1 = [[0] * m for _ in range(n)]
     
     != matrix_2 = [[0] * m] * n
     # 왜 다른가?
     # [0]*m 를 n번 곱하게 되면 주소값이 동일
     # matrix_2[0][0] = 1 하면
     # ㅡ[[1, 0, 0], [1, 0, 0], [1, 0, 0]] 이 됨
     ```

- 문자열을 리스트로 변환했을 때
  
  ```python
  a = 'adfasdfasdf'
  b = list(a)
  print(b)
  
  >>> ['a','d','f','a','s','d','f','a','s','d','f']
  ```

## 입력 받기

1. 행렬의 크기가 미리 주어지는 경우
   
   ```python
   # 3 x 3 크기의 입력을 받아보자
   # 1 2 3
   # 4 5 6 
   # 7 8 9
   matrix = []
   for _ in range(3):
       line = list(map(int,input().split()))
       matrix.append(line)
   ```

   [list(map(int, input().split())) for _ in range(3)]

```
2. 행렬의 크기가 입력으로 주어지는 경우

```python
n, m = input().split()
[list(map(int, input().split()) for _ in range(N)]
```

n, m = input().split()

[list(map(int, input().split())) for _ in range(n)]
