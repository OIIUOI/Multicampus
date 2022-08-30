nums = list(map(int, input().split()))
jud = 0
for i in range(len(nums)-1):
    if nums[i] == nums[i+1] - 1:
        jud += 1
    elif nums[i] == nums[i+1] +1:
        jud-= 1
    else:
        jud+=20

if jud == 7:
    print('ascending')
elif jud == -7:
    print('descending')
else:
    print('mixed')