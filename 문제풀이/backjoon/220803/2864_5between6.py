a, b = input().split()

min_a = int(a.replace('6', '5'))
min_b = int(b.replace('6', '5'))

max_a = int(a.replace('5', '6'))
max_b = int(b.replace('5', '6'))

print(min_a + min_b, max_a + max_b)