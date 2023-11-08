# 새로운 불면증 치료법

'''
str = set("Hello")
str
{'e', 'H', 'l', 'o'}
'''
# T = int(input())
#
# for i in range(1, T+1):
#     N = int(input())
#
#     check_set = set()
#     multiplier = 1
#
#     while len(check_set) < 10:
#         current_number = N * multiplier
#         check_set.update(str(current_number))
#
#         multiplier += 1
#
#     last_sheep = N * (multiplier - 1)
#     print(f'#{i} {last_sheep}')

# ===============================================================
# 방법 2
# ===============================================================
for t in range(int(input())):
 n = int(input())
 s = set(str(n))
 i = 1
 while len(s) < 10:
  i += 1
  s.update(str(n*i))
 print(f'#{t+1} {i*n}')
