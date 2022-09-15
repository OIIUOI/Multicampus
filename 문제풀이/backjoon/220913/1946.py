import sys
input = sys.stdin.readline

for _ in range(int(input())):
    memb = []
    mem_len = int(input())

    for _ in range(mem_len):
        pap, mtm = map(int, input().split())
        memb.append((pap,mtm))
    
    s_memb = sorted(memb, key=lambda x: x[0])
    
    standard = s_memb[0][1]
    cnt = 1

    for i in range(mem_len):
        if s_memb[i][1] < standard:
            cnt += 1
            standard = s_memb[i][1]
    print(cnt)