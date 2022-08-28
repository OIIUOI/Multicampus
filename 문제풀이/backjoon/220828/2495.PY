for _ in range(3):
    num = input()
    cnt = 1
    cnt_list = []
    for i in range(len(num)-1):
        if num[i] == num[i + 1]:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1
    cnt_list.append(cnt)
    print(max(cnt_list))