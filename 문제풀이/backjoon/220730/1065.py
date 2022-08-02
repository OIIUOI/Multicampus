N = int(input())
cnt = 0

for n in range(1, N+1):
    n = str(n)
    if int(n) < 100:
        cnt += 1
    elif int(n[0]) - int(n[1]) == int(n[1]) - int(n[2]):
        cnt += 1
print(cnt)