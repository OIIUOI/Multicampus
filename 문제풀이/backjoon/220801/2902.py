name = input().split('-')
final = []
print(type(final))
for n in name:
    final = final.append((n[0]))
s_name = ''.join(final)
print(s_name.upper())
