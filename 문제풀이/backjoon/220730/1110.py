N = input()

if int(N) < 10:
    N = '0' + N

def n_num(x):
    z = str((int(x[0]) + int(x[1])) % 10)
    y = x[1] + z[0]
    return y


temp = N
cnt = 0
while (N != temp) or (cnt == 0):
    cnt += 1
    temp = n_num(temp)

print(cnt)