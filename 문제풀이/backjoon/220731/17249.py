x, y = input().split('(^0^)')
cnt_a = 0
cnt_b = 0
for a in x:
    if a =='@':
        cnt_a += 1
for b in y:
    if b =='@':
        cnt_b += 1
print(cnt_a, cnt_b)