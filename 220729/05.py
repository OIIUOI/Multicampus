import sys
sys.stdin = open("05_creditcard_2.txt")

card = ''
for t in range(1, int(input())+1):
    nums = list(map(str, input().split('-')))
    card = ''
    for n in nums:
        card += n
    check_l = [3, 4, 5, 6, 9]
    if len(card) != 16:
        print(f'#{t} 0')
    elif int(card[0]) in check_l:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')