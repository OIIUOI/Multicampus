s, k, h = map(int, input().split())
u_list = [s, k, h]
if sum(u_list) >= 100:
    print('OK')
else:
    if s == min(u_list):
        print('Soongsil')
    elif k == min(u_list):
        print('Korea')
    else:
        print('Hanyang')
