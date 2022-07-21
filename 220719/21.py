a = 1234
jali = -1
b = a
while b > 1:
    b = b / 10
    jali += 1

s_list = []
for i in range(jali, -1, -1):
    temp = a // (10 ** i)
    a = a - (10 ** i)* temp
    s_list.append(temp)

s_list.reverse()
n_list = []

for i in range(0, jali + 1):
    tem = s_list[i] * (10 ** (jali - i))
    n_list.append(tem)

print(sum(n_list))
