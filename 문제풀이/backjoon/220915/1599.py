import sys
input = sys.stdin.readline
order = {'a':'a', 'b':'b', 'k':'c', 'd':'d', 'e':'e', 'g':'f', 'h':'g',
 'i':'h', 'l':'i', 'm':'j', 'n':'k', '0':'l', 'o':'m',
 'p':'n', 'r':'o', 's':'p', 't':'q', 'u':'r', 'w':'s', 'y':'t'}

def change_alpha(word):
    result = ''
    for w in word:
        result += order[w]
    return result

words = {}
for _ in range(int(input().strip())):
    word = input().strip().replace('ng','0')
    words[change_alpha(word)] = word.replace('0','ng')

sort_word = []
for key in words.keys():
    sort_word.append(key)

sort_word.sort()

for s in sort_word:
    print(words[s])
