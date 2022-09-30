import sys

input = sys.stdin.readline
start, end, final = input().strip().split()

join = set()
result = 0

while True:
    try:
        time, name = input().strip().split()
        if start >= time:
            join.add(name)
        elif end <= time <= final:
            if name in join:
                result += 1
                join.remove(name)
    except:
        break

print(result)
