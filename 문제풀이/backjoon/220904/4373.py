natural_num = list(range(1,10001))
generate_num = set()

for i in range(1, 10001):
    total = i
    for j in str(i):
        total += int(j)
        if total > 10001:
            break
    generate_num.add(total)


self_num = sorted(list(set(natural_num) - generate_num))
for s in self_num:
    print(s)