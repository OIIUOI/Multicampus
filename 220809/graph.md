# 그래프

## 그래프에 대한 이해

> 정점(Vertex)과 이를 연결하는 간선(Edge)들의 
> 
> 집합으로 이루어진 비선형 자료구조



| 용어  |                  |                               |
|:---:| ---------------- | ----------------------------- |
| 정점  | **Vertex, Node** | 간선으로 연결되는 객체                  |
| 간선  | **Edge**         | 정점 간의 관계(연결)를 표현하는 선을 의미      |
| 경로  | **Path**         | 시작 정점부터 도착 정점까지 거치는 정점을 나열한 것 |
| 인접  | **Adjacency**    | 두 개의 정점이 하나의 간선으로 직접 연결된 상태   |



## 그래프의 종류

### 1. 무방향 그래프

**Undirected graph**

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2022-08-10-01-31-52-image.png" title="" alt="" width="374">

- 간선의 방향이 없는 가장 일반적인 그래프

- 간선을 통해 양방향의 정점 이동 가능

- 차수(Degree) : 하나의 정점에 연결된 간선의 개수

- 모든 정점의 차수의 합 = 간선 수 * 2



### 2. 유방향 그래프

**Directed graph**

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2022-08-10-01-34-39-image.png" title="" alt="" width="379">

- 간선의 방향이 있는 그래프

- 간선의 방향이 가리키는 정점으로 이동 가능

- 차수(Degree) : 진입 차수와 진출 차수로
  
  - 진입차수(In-degree) : 외부 정점에서 한 정점으로 들어오는 간선의 수
  
  - 진출차수(Out-degree) : 한 정점에서 외부 정점으로 나가는 간선의 수



## 그래프의 표현

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-11-17-image.png)

### 1. 인접 행렬

**Adjacentt matrix**

> 두 정점을 연결하는 간선이 없으면 0, 있으면 1을 가지는 행렬로 표현하는 방식

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-34-35-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-33-11-image.png)



### 2. 인접 리스트

**Adjacent list**

> 리스트를 통해 각 정점에 대한 인접 정점들을 순차적으로 표현하는 방식

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-35-30-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-35-58-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-38-41-image.png)



## 인접 행렬 vs 인접 리스트

인접 행렬은 직관적이고 만들기 편하지만 불필요하게 공간이 낭비됨

인접 리스트는 연결된 정점만 저장하여 효율적이므로 자주 사용된다

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-08-10-02-40-11-image.png)
