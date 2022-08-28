import sys
input = sys.stdin.readline
count = 0
for _ in range(int(input())):
    a = input()
    if a == 'ENTER\n':
        hi_dic = {}
    if a not in hi_dic:
        hi_dic[a] = 1
        count += 1
print(count)