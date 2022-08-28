import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c = input()
    a = list(map(int, input().split()))
    c = int(input())
    b = list(map(int, input().split()))
    for q in b:
        if q in a:
            print(1)
        else:
            print(0)