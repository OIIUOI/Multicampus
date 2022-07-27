t = int(input())

for i in range(1, t + 1):
    ml = list(map(int, input().split()))
    print(f'#{i} {round(sum(ml)/10)}')