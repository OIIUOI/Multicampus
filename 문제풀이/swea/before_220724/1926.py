N = input()
for i in range(1, int(N) + 1):
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        c = 0
        for j in str(i):
            if (j == '3') or (j == '6') or (j == '9'):
                c += 1
            else:
                continue
        print('-'*c, end = ' ')    
    else:
        print(i, end = ' ')