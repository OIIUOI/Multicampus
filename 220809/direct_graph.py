from pprint import pprint
n, m = map(int, input().split())
mr = [[] for _ in range(n+1)]
am = [[0] *(n + 1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    mr[u].append(v)
    am[u][v] = 1

pprint(am)
print(mr)