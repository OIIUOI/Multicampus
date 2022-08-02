import sys
sys.stdin = open("06_cipher.txt")

length = int(input())
code = input().split()
origin = {}

# 암호문 origin 딕셔너리에 입력
for i in range(length):
    origin[i] = code[i]

order_time = int(input())
order = input().split('|')

for ot in range(order_time):
    for o in order:
        # 스플릿아 3개로 쪼개줘 할 줄 모른다구
        x,y,z = o.split('',3)
        origin[x] = z
