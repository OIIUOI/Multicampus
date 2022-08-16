import sys

node = int(sys.stdin.readline())

n1, n2 = map(int, sys.stdin.readline().split())

edge = int(sys.stdin.readline())
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    n, m = map(int, sys.stdin.readline().split())
    graph[n].append(m)
    graph[m].append(n)

visit = ['x' for _ in range(node + 1)]
def dfs(start,end):
    sign = [start]
    visit[start] = 'o'

    while sign:
        now = sign.pop()
        for g in graph[now]:
            cnt = 0
            if visit[g] == 'x':
                visit[g] = 'o'
                sign.append(g)
                cnt += 1
            if visit[end] == 'o':
                return cnt
        else:
            return -1
                
                

print(dfs(n1, n2))