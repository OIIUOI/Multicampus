total = 0
m_list = [int(input()) for _ in range(10)]

for m in m_list:
    total += m
    if total >= 100:
        if abs(total-100) <= abs(total - m - 100):
            print(total)
            break
        else:
            print(total - m)
            break