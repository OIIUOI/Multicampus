from collections import deque

card = deque([a for a in range(1, int(input())+1)])

while len(card) > 1:
    print(card.popleft(), end = ' ')
    card.append(card.popleft())
print(card[0])

