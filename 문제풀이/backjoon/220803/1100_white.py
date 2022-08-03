from pprint import pprint

chess = [list(input()) for _ in range(8)]
horse = 0

for i in range(8):
   for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                if chess[i][j] == 'F':
                    horse += 1
        else:
            if j % 2 == 1:
                if chess[i][j] == 'F':
                    horse += 1
print(horse)