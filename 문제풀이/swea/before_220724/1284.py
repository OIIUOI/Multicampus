time = int(input())

for t in range(1, time + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    
    if W <= R:
        B = Q
    else:
        B = Q + S * (W - R)
    
    if A > B:
        print(f'#{t} {B}')
    else:
        print(f'#{t} {A}')