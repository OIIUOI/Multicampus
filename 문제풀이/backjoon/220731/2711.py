for _ in range(int(input())):
    n, word = input().split()
    word = word.upper()
    rm_word = word.replace(word[int(n)],'')
    print(rm_word)