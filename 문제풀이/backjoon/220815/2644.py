node = int(input())
n1, n2 = map(int, input().split())
edge = int(input())
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    na, nb = map(int, input().split())
    graph[na].append(nb)
    graph[nb].append(na)

visit = [False for _ in range(node + 1)]
def dfs(a, b, cnt):
    visit[a] = True
    if visit[b]: # 만약 b를 방문했다면
        return cnt
    for adj in graph[a]:
        if not visit[adj]: # 만약 방문을 안 했으면
            cnt += 1
            dfs(adj, b, cnt)
    return -1




print(dfs(n1,n2,0))