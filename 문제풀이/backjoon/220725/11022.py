time = int(input())

for t in range(1, time + 1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a} + {b} = {a+b}')