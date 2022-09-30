import sys

input = sys.stdin.readline
car = {}
out = []
cnt = 0

num = int(input())
for i in range(num):
    car[input().rstrip()] = i

for j in range(num):
    outcar = input().rstrip()
    out.append(car[outcar])

for i in range(num - 1):
    for j in range(i + 1, num):
        if out[i] > out[j]:
            cnt += 1
            break

print(cnt)
