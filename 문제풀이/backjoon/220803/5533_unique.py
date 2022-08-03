from pprint import pprint
# 게임 리스트 중복값 0 처리

person = int(input())

# 게임별 점수 리스트
score = [[],[],[]]

for _ in range(person):
    x, y, z = map(int, input().split())
    score[0].append(x)
    score[1].append(y)
    score[2].append(z)
# 게임별 점수리스트에 값을 넣었음
# 개인별 score[p][0] 값이 score[p].count(score[p][0]) == 1 일때
# sum_t 에 더해줘야 함
for p in range(person):
    sum_t = 0
    for i in range(3):
        if score[i].count(score[i][p]) == 1:
            sum_t += score[i][p]
    print(sum_t)




















# 세로열에 있는 걸 리스트 안 쓰고 반복문으로 사인걸고 확인
#person = int(input())
#li = [list(map(int, input().split())) for _ in range(person)]
#for p in range(person):
#    s = 0
#    for g in range(3):
#        t = li[p][g]
#        ok = 1
#        for k in range(person):
#            if k == p:
#                continue
#            if li[k][g] == t:
#                ok = 0; break
#        if ok == 1:
#            s += t
#    print(s)

# 게임 별 리스트를 만들어서 해당 점수의 카운트가 1인 경우에만
# 합치면 된다
#n = int(input())
#score = [[], [], []]
#sum = []
#for i in range(n):
#    a, b, c = map(int, input().split())
#    score[0].append(a)
#    score[1].append(b)
#    score[2].append(c)
#for i in range(n):
#    s_score = 0
#    for j in range(3):
#        if score[j].count(score[j][i]) == 1:
#            s_score += score[j][i]
#    print(s_score)
