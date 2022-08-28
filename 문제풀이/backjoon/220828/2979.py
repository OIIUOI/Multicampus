a, b, c = map(int, input().split())
ar_x, le_x = map(int, input().split())
ar_y, le_y = map(int, input().split())
ar_z, le_z = map(int, input().split())

x = list(range(ar_x, le_x))
y = list(range(ar_y, le_y))
z = list(range(ar_z, le_z))

t_list = [ar_x, le_x, ar_y, le_y, ar_z, le_z]
tax_cnt = 0
total = 0
for t in range(1, max(t_list)):
    tax_cnt = 0
    if t in x:
        tax_cnt += 1
    if t in y:
        tax_cnt += 1
    if t in z:
        tax_cnt += 1
    if tax_cnt == 1:
        total += a
    elif tax_cnt == 2:
        total += (b * 2)
    elif tax_cnt == 3:
        total += (c * 3)
print(total)