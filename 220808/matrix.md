# 이차원 리스트

## 완전탐색

### 1. 무식하게 다해보기 (Brute-force)

모든 경우의 수를 탐색하여 문제를 해결하는 방식

- 브루트포스라고도 하며 무식하게 밀어붙인다는 뜻이다

- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해서 풀 수 있다

- 복잡한 알고리즘 보다는 아이디어를 어떻게 코드로 구현할 것인지가 중요하다

```python
# 블랙잭 가장 큰 문제를 통해 완전탐색 이해하기
# N = 3인 경우
def blackjack(n, m, cards):
  max_total = 0
  # 완전탐색
  for i in range(n - 2):
    for j in range(i + 1, n - 1):
      for k in range(j + 1, n):
        total = cards[i] + cards[j] + cards[k]
        # 현재 가장 큰 값보다는 크고, m은 넘지 않아야 갱신
        if max_total < total <= m:
          max_total = total
        # 합이 m과 같으면 탐색할 의미가 없으므로 종료
        if total == m:
          return total

  return max_total
```

### 2. 델타 탐색 (Delta Search)

이차원 리스트의 모든 원소를 순회 (완전탐색)하며, 

각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식

- 이차원 리스트의 `인덱스(좌표)의 조작` 을 통해서 상하좌우 탐색을 한다. 이때 행과 열의 변량인 `-1, +1을 델타(delta)값` 이라 한다.

| 좌상, 좌, 좌우      | 상, 기준, 하   | 우상, 우, 우하      |
| -------------- | ---------- | -------------- |
| (x - 1, y - 1) | (x - 1, y) | (x - 1, y + 1) |
| (x, y - 1)     | (x, y)     | (x, y + 1)     |
| (x + 1, y - 1) | (x + 1, y) | (x + 1, y + 1) |

```python
# 행을 x, 열을 y로 표현
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 한번에 튜플로 사용하기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(4):
    for j in range(4):
        for d in delta:
            print(i + d[0], j + d[1])


# 상 하 좌 우 이동을 간단히 표현하기
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 범위를 벗어나지 않으면서 갱신
    if 0 <= nx < 3 and 0 <= ny < 3:
        x = nx
        y = ny


# 총 정리 코드
# 1. 델타 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 2. 이차원 리스트 순회
for x in range(n):
    for y in range(m):
        # 3. 델타값을 이용해 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 4. 범위를 벗어나지 않으면서 갱신
            if 0 <= nx < n and 0 <= ny < m:
                x = nx
                y = ny
                print(x, y)
```
