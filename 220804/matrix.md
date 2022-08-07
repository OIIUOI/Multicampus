# 이차원 리스트

1. 이차원 리스트

2. 입력받기

3. 순회

4. 전치

5. 회전

---

## 순회

1. 이중 for문을 이용한 행 우선 순회
   
   ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-04-11-21-01-image.png)

```python
for row in matrix:
    print(row)
>>> [1, 2, 3, 4]
    [5, 6, 7, 8]
    [9, 0, 1, 2]

for row in matrix:
    for elem in row:
        print(elem, end = ' ')
    print()
>>> 1 2 3 4
    5 6 7 8
    9 0 1 2
```

   

2. 이중 for문을 이용한 열 우선 순회
   
   ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-04-11-19-45-image.png)

---

                                           **행 우선 순회 VS 열 우선 순회**

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-04-11-25-08-image.png)

---

- 파이써닉한 방법으로 이차원 리스트의 총합 구하기
* ![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-04-11-36-10-image.png)

행 우선 순회를 이용해 이차원 리스트의 최대값, 최소값 구하기

- 2차원 리스트의 최대값 구하기
  
  ```python
  # 3 x 4 행렬
  matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2] ]
  
  # 방법1) 행 우선 순회를 이용한 방법
  max_val = 0
  for r in range(3):
      for c in range(4):
         if matrix[r][c] > max_val:
            max_val = matrix[r][c]  
  # 방법2) pythonic한 방법
   max_val = max(map(max, matrix))
  ```

---

## 전치(transposed)

전치란 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다

열 우선순위 했다

```python
# 3 x 4 행렬
matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2] ] transposed_matrix = [[0] * 3 for _ in range(4)] for c in range(4):    for r in range(3):       transposed_matrix[c][r] = matrix[r][c]  # transposed_matrix = [
 #   [1, 5, 9],
 #   [2, 6, 0],
 #   [3, 7, 1],
 #   [4, 8, 2]
 # ]
```

---

## 회전

- 왼쪽으로 90도 회전하기

```python
# 3 x 3 행렬
matrix = [   [1, 2, 3],   [4, 5, 6],   [7, 8, 9]]

rotated_matrix = [[0] * 3 for _ in range(3)]

for c in range(3):   for r in range(3):      rotated_matrix[c][r] = matrix[r][3 - c - 1]

# rotated_matrix = [
#   [3, 6, 9],
#   [2, 5, 8],
#   [1, 4, 7]
# ]
```

- 오른쪽으로 90도 회전하기

```python
# 3 x 3 행렬
matrix = [   [1, 2, 3],   [4, 5, 6],   [7, 8, 9]]

rotated_matrix = [[0] * 3 for _ in range(3)]

for c in range(3):   for r in range(3):      rotated_matrix[c][r] = matrix[3 - r - 1][c]

# rotated_matrix = [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
```
