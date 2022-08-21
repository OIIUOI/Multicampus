import sys

node = int(sys.stdin.readline())

n1, n2 = map(int, sys.stdin.readline().split())

edge = int(sys.stdin.readline())
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    n, m = map(int, sys.stdin.readline().split())
    graph[n].append(m)
    graph[m].append(n)


visit = [False for _ in range(node + 1)]

chon = 0
result = -1
sign = [(n1, chon)]

visit[n1] = True

while sign:
    print(visit)
    print(f'sign {sign}')
    now = sign.pop()[0]
    print(f'now {now}')
    if now == n2:
        print(chon)
        break
    for g in graph[now]:
        print(visit)
        if not visit[g]:
            visit[g] = True
            sign.append((g, chon))

