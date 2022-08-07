year_17 = [
    5000000, *([3000000]*2), *([2000000]*3),
    *([500000]*4), *([300000]*5), *([100000]*6)
]
year_18 = [
    5120000, *([2560000]*2), *([1280000]*4),
    *([640000]*8), *([320000]*16)
]

for t in range(int(input())):
    a, b = map(int, input().split())
    total = 0
    if (0 < a < 22) and (0 < b < 32):
        total = year_17[a-1] + year_18[b-1]
    elif 0 < a < 22:
        total = year_17[a-1]
    elif 0 < b < 32:
        total = year_18[b-1]
    print(total)
