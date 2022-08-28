for t in range(1, int(input())+1):
    cls = list(map(int, input().split()))
    ccnt= cls.pop(0)
    s_cls = sorted(cls, reverse = True)
    gap = []
    for i in range(len(s_cls)-1):
        g = s_cls[i] - s_cls[i+1]
        gap.append(g)
    print(f'Class {t}')
    print(f'Max {max(cls)}, Min {min(cls)}, Largest gap {max(gap)}')