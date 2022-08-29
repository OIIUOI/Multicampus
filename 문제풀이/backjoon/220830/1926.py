import sys
input = sys.stdin.readline

h, w = map(int, input().split())

board = []
for _ in range(h):
    a = list(map(int, input().split()))
    board.append(a)

def dfs(graph, x, y):
    stack = [(x,y)]
    picture_wide = 1
    graph[x][y] = 0
    while stack:
        a, b = stack.pop()
        dy = [1, 0]
        dx = [0, 1]
        for i in range(2):
            ny = b + dy[i]
            nx = a + dx[i]
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                picture_wide += 1
                stack.append((nx,ny))
    return picture_wide

pic_list = []
cnt = 0
for q in range(h):
    for p in range(w):
        if board[q][p] == 1:
            cnt += 1
            pic = dfs(board, q, p)
            pic_list.append(pic)
print(cnt)
print(max(pic_list))