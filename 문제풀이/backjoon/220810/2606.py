com_num = int(input())
edge = int(input())
# 지도
graph = [[] for _ in range(com_num + 1)]

for _ in range(edge):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

# 일지
diary = ['X' for _ in range(com_num + 1)]

# 행동양식
def dfs(start):
    # 표지판 
    sign = [start] # 표지판 세우기
    diary[start] = 'O' # 방문도장 찍기

    while sign: # 표지판 다 뽑을때까지
        now = sign.pop() # 표지판 뽑아서 GPS로 쓸꺼에옹
        for g in graph[now]: # 인접 노드 지도에서 gps 찍어서 확인
            if diary[g] == 'X': # 인접노드에 안갔다면
                diary[g] = 'O' # 가서 노트적고
                sign.append(g) # 표지판 세운다

dfs(1)
print(diary.count('O')-1)