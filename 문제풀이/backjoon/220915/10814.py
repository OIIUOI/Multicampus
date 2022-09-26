member = []
for _ in range(int(input())):
    age,name = input().split()
    member.append((age,name))

member.sort(key= lambda x:int(x[0]))

for m in member:
    print(m)
