num = input()
cnt = 0
while len(num) != 1:
    cnt += 1
    result = 0
    for n in num:
        result += int(n)
    num = str(result)

print(cnt)

if int(num)%3 == 0:
    print('YES')
else:
    print('NO')