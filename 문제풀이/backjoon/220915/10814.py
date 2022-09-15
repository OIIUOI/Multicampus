member = []
for _ in range(int(input())):
    person = input()
    member.append((person))

member.sort(key= lambda x:int(x.split()[0]))

for m in member:
    print(m)