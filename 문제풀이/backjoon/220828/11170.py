for _ in range(int(input())):
    cnt = 0
    n, m = map(int, input().split())
    for a in range(n, m+1):
        for a1 in str(a):
            if a1 == '0':
                cnt += 1
    print(cnt)
