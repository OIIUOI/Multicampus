n = int(input())
open_board = [list(input()) for _ in range(n)]
click_board = [list(input()) for _ in range(n)]

see_board = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if click_board[i][j] == 'x' and open_board[i][j] =='.':
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]
            
            mine = 0
            for p in range(8):
                nx = j + dx[p]
                ny = i + dy[p]
                if 0 <= nx < n and 0 <= ny < n:
                    if open_board[ny][nx] == '*':
                        mine += 1
            see_board[i][j] = mine
        elif click_board[i][j] == 'x' and open_board[i][j] =='*':
            for x in range(n):
                for y in range(n):
                    if open_board[x][y] == '*':
                        see_board[x][y] = '*'

for q in range(n):
    print(''.join(map(str, see_board[q])))
