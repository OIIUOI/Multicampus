card_len, total = map(int, input().split())
card_list = list(map(int, input().split()))
sum_list = []
for i in range(card_len-2):
    for j in range(i+1, card_len-1):
        for k in range(j+1, card_len):
            card_sum = card_list[i] + card_list[j] + card_list[k]
            sum_list.append(card_sum)

near = 0
for s in sum_list:
    if total == s:
        near = s
        break
    elif total - s < 0:
        pass
    elif total - near > total - s:
        near = s
print(near)