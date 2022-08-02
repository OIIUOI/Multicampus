import sys
sys.stdin = open("04_rectangle.txt")

for t in range(1, int(input()) + 1):
    rec_list = list(map(int, input().split()))
    rec_dict = {}
    for r in rec_list:
        if r not in rec_dict:
            rec_dict[r] = 1
        elif r in rec_dict:
            rec_dict[r] += 1

    for e in rec_dict:
        if rec_dict[e] == 1:
            print(f'#{t} {e}')
        elif rec_dict[e] == 3:
            print(f'#{t} {e}')
