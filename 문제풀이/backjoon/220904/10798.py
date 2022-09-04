for i in range(1,6):
    globals()['a{}'.format(i)] = list(input())

for i in range(15):
    try:
        print(a1[i], end='')
    except:
        pass
    try:
        print(a2[i], end='')
    except:
        pass
    try:
        print(a3[i], end='')
    except:
        pass
    try:
        print(a4[i], end='')
    except:
        pass
    try:
        print(a5[i], end='')
    except:
        pass