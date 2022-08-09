# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접리스트로 표현
# 첫째 줄에 정점의 개수 N, 간선의 개수 M 주어짐 
# 둘째줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어짐 
# 인접 행렬 출력, 인접 리스트 출력 

import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
mr = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    mr[u].append(v)
    mr[v].append(u)

print(mr)
