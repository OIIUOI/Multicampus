for _ in range(int(input())):
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    total_move = 0
    for i in range(n):
        first_judge = 0
        movelen = 1
        for j in range(m):
            # 세로로 세겠다
            # 처음 박스를 만난 이후로 흰칸을 세는데, 중간에 검은 칸을 만나면 
            # 더해지는 movelen이 커진다
            # 해서 한꺼번에 세버리게끔

            if board[j][i] == 1 and first_judge == 0:
                first_judge = 1
            elif board[j][i] == 1 and first_judge == 1:
                movelen += 1
            elif board[j][i] == 0 and first_judge == 1:
                total_move += movelen
    print(total_move)



