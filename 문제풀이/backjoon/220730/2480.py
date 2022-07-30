from collections import Counter
A= list(map(int, input().split()))
B = {}
for a in A:
    if a not in B:
        B[a] = 1
    else:
        B[a] += 1
C = Counter(A).most_common(1)[0][0]
D = max(A)
if 3 in B.values():
    print(10000 + C * 1000)
elif 2 in B.values():
    print(1000 + C * 100)
else:
    print(D * 100)