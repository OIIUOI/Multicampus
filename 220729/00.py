import sys

sys.stdin = open("00_most_num.txt")

for _ in range(1,int(input())+ 1):
  a = int(input())
  # 넘겨준 숫자를 리스트로 받음
  num_list = list(map(int, input().split()))
  cnt_dict = {}
  max_num = []
  # 리스트 순회하며 key에 점수, value에 빈출값
  for n in num_list:
    if n in cnt_dict:
      cnt_dict[n] += 1
    else:
      cnt_dict[n] = 1
  # 최대빈출값에 해당하는 밸류값 순회하면서 찾기
  for v in cnt_dict:
    if max(cnt_dict.values()) == cnt_dict[v]:
      max_num.append(v)
  b = max(max_num)
  print(f'#{a} {b}')
