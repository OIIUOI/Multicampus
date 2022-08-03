n, m = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    total = 0
    for a in range(i, x):
        for b in range(j, y):
            total += origin[a][b]
    print(total)