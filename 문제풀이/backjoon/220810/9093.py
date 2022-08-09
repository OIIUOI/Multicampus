for _ in range(int(input())):
    sent = list(input().split())
    for s in sent:
        print(s[::-1], end = ' ')
    