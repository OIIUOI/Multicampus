import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stack_ = [] 
sign = 1

for i in range(m):
    ki = int(input())
    stack_.append(list(map(int, input().split())))

for i in range(m):
    for j in range(len(stack_[i]) - 1):
        if stack_[i][j] < stack_[i][j + 1]:
            sign = 0

if sign == 0:
    print('No')
else:
    print('Yes')