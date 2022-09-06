import sys
input = sys.stdin.readline

lis, seen = map(int, input().split())

lis_li = []
seen_li = []
for _ in range(lis):
    a = input().rstrip()
    lis_li.append(a)
for _ in range(seen):
    b = input().rstrip()
    seen_li.append(b)

inter = list(set(lis_li) & set(seen_li))
inter.sort()
print(len(inter))
for i in inter:
    print(i)
