import sys
input = sys.stdin.readline

time = int(input())
dots = list(map(int, input().rstrip().split()))
# 순서대로 정렬
dot_order = sorted(list(set(dots)))
# 시간복잡도 때문에 딕셔너리로 변환
di = {dot_order[i] : i for i in range(len(dot_order))}

for d in dots:
    print(di[d], end = ' ')