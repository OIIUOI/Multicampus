num_list = []
for t in range(1,6): 
    if 'FBI' in input():
        num_list.append(t)
if num_list:
    print(*num_list)
else:
    print('HE GOT AWAY!')