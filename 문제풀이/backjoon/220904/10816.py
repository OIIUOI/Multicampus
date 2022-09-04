import sys
input = sys.stdin.readline
from collections import Counter

card_num = int(input())
card_list = list(map(int, input().split()))
card = Counter(card_list)
time = int(input())
check_list = list(map(int, input().split()))

for check in check_list:
    if check in card:
        print(card[check], end = ' ')
    else:
        print(0, end = ' ')