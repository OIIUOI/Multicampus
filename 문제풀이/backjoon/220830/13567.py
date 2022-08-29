square, time = map(int, input().split())
for _ in range(time):
    direct, num = input().split()
    num = int(num)

    board = [[]*square for _ in range(square)]
    