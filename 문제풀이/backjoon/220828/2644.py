people = int(input())
start, goal = map(int, input().split())

graph = [[] for _ in range(people+1)]

for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visit = [False] * (people + 1)
stack = []

visit[start] = True
stack.append((start,0))
answer = -1
while stack:
    now, cnt = stack.pop()
    if now == goal:
        answer = cnt
        break
    for g in graph[now]:
        if not visit[g]:
            visit[g] = True
            stack.append((g, cnt + 1))
print(answer)

