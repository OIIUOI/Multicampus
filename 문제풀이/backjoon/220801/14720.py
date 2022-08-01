n = input()
milk_list = list(map(int, input().split()))
cnt = 0
a = 0
for m in milk_list:
    if m == a:
        cnt += 1
        a += 1
    if a == 3:
        a = 0
print(cnt)