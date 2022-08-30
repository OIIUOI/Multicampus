for _ in range(int(input())):
    i, word = input().split()
    i = int(i)-1
    lw = list(word)
    lw.pop(i)
    print(''.join(lw))