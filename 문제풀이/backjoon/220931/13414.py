import sys

input = sys.stdin.readline

cut, all = map(int, input().split())
inroment = {}

for i in range(all):
    student = input().strip()
    inroment[student] = i

cut_list = sorted(inroment.items(), key=lambda x: x[1])

for cl in cut_list[:cut]:
    print(cl[0])
