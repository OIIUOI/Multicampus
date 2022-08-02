del_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

word = input().upper()
trans_word = ''
for w in word:
    if w not in del_list:
        trans_word += w
print(trans_word)