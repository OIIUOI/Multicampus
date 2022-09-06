import sys

input = sys.stdin.readline

book_dic = {}
time = int(input())
for _ in range(time):
    book = input().rstrip()
    if book in book_dic:
        book_dic[book] += 1
    else:
        book_dic[book] = 1

top_b = []
for key,value in book_dic.items():
    if value == max(book_dic.values()):
        top_b.append(key)

print(sorted(top_b)[0])