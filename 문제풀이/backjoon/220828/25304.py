total = int(input())
realpay = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    realpay += x * y
if total == realpay:
    print('Yes')
else:
    print('No')