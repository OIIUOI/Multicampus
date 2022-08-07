p, x = map(int, input().split())
cnt = 1
while p != x:
    x += 1
    cnt += 1
print(cnt)