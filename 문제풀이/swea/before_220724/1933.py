i = 1
N = int(input())

while i != N + 1:
    if N % i == 0:
        print(i, end = ' ')
    i += 1