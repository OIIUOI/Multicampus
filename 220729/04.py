import sys
sys.stdin = open("04_creditcard_1.txt")

for t in range(1, int(input()) + 1):
    num_list = list(map(int,input().split()))
    total = 0
    for i in range(1, 16):
        if i % 2 == 1:
            total += (num_list[i-1]*2)
        else:
            total += num_list[i-1]
    N = 10 - (total % 10)
    if N == 10:
        N = 0
    print(f'#{t} {N}')
