import sys
input = sys.stdin.readline

# 숫자이면 변환해주는 함수
def sum_num(x):
    result = 0
    for i in x:
        if i in number:
            result += int(i)
    return result

number = ['0','1','2','3','4','5','6','7','8','9']
guitar = []

for _ in range(int(input())):
    guitar.append(input().rstrip())
    
guitar.sort()
guitar.sort(key=sum_num)
guitar.sort(key= len)

for g in guitar:
    print(g)