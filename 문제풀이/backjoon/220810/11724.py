import sys

node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit = ['x' for _ in range(node + 1)]

def dfs(start):
    sign = [start]
    visit[start] = 'o'

    while sign:
        now = sign.pop()
        for g in graph[now]:
            if visit[g] == 'x':
                visit[g] = 'o'
                sign.append(g)

cnt = 0

for i in range(1,node + 1):
    if visit[i] == 'x':
        dfs(i)
        cnt += 1
    
print(cnt)
