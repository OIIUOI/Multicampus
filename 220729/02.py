import sys
sys.stdin = open("02_mirror_image_of string.txt")

# 대응하는 문자 딕셔너리에 넣어 놓고
# 거울상의 이미지이므로 reverse 하고
# for문으로 돌린다

mirror_dic = {
    'b':'d', 'd':'b', 'p': 'q', 'q':'p'
}

for t in range(1, int(input()) + 1):
    word = input()[::-1]
    m_word = ''
    for w in word:
        m_word += mirror_dic[w]
    print(f'#{t} {m_word}')