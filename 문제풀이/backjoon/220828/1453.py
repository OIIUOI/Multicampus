time = int(input())
PC_list = list(map(int, input().split()))

cnt = 0
for i in range(len(PC_list)-1):
    for j in range(i+1, len(PC_list)):
        if PC_list[i] == PC_list[j]:
            cnt += 1
            break

print(cnt)