def dic_w(word):
    dic = dict()
    for w in word:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
    return dic

for _ in range(int(input())):
    word1, word2 = input().split()
    a = dic_w(word1)
    b = dic_w(word2)
    if a == b:
        print(f'{word1} & {word2} are anagrams.')
    else:
        print(f'{word1} & {word2} are NOT anagrams.')


