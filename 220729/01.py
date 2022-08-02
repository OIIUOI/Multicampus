import sys
sys.stdin = open("01_income_imbalance.txt")

time = int(input())
for t in range(1, time + 1 ):
    div = int(input())
    inc_list = list(map(int, input().split()))
    average = sum(inc_list) / div
    cnt = 0
    # 수입리스트 순회하며 평균보다 낮거나 같으면 cnt + 1
    for inc in inc_list:
        if inc <= average:
            cnt += 1
    print(f'#{t} {cnt}')