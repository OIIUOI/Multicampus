n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]

cnt = 0
cnt_1 = 0

for i in range(n):
    if 'X' not in castle[i]:
        cnt += 1

for j in range(m):
    if 'X' not in [castle[i][j] for i in range(n)]:
        cnt_1 += 1

print(max(cnt, cnt_1))