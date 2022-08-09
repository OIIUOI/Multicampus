
import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
mr = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    mr[u].append(v)

print(mr)

# 0 노드가 없어서 레인지 에러가 생기는 것 같은데 어떻게 해결을 해야 할 지 모르겠음