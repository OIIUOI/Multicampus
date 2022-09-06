incom = {}
for _ in range(int(input())):
    a, b = input().split()
    if b == 'enter':
        incom[a] = 1
    else:
        incom.pop(a)

incom = list(incom.keys())
incom.sort(reverse = True)

for a in incom:
    print(a)