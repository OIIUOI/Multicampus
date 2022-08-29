import sys
sys.stdin = open('1206.txt')
input = sys.stdin.readline

for t in range(1,11):
    num_b = int(input())
    building = list(map(int, input().split()))
    cnt = 0
    for i in range(2,num_b-2):
        buildings= [building[i-2], building[i-1], building[i], building[i+1], building[i+2]]
        ifbuildings = [building[i-2], building[i-1], building[i+1], building[i+2]]
        if max(buildings) == building[i] and max(ifbuildings) != building[i]:
            cnt += building[i] - max(ifbuildings)
    print(f'#{t} {cnt}')
