time = int(input())

for t in range(1, time + 1):
   N = int(input())
   my_set = set()
   num = 1
   while len(my_set) < 10:
       total_cnt = str(N * num)
       num += 1
       for a_s in total_cnt:
           my_set.add(a_s)
   print(f'#{t} {int(total_cnt)}')