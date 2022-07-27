time = int(input())
total = 0

for t in range(1, time + 1):
    N = int(input())
    total = 0
    for i in range(1, N + 1):
        j = (-1) ** (i - 1)
        total += i * j
    print(f'#{t} {total}')