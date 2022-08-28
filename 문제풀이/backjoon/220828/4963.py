from xmlrpc.server import DocXMLRPCRequestHandler


while True:
    if input() == "0 0":
        break
    n, m = map(int, input().split())
    
    board = []
    for _ in range(m):
        b = list(map(int, input().split()))
        board.append(b)
    cnt = 0
    dx = [1, 1, 1, -1, 0] 
    dy = [0, -1, 1, 1, 1] 
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1 # 섬의 개수를 세고
                for k in range(5):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[ny][nx] == 1: # 연결된 육지를 모조리 바다로 바꾼다
                            board[ny][nx] = 0
                        
                            



