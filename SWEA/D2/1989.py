# 초심자의 회문 검사
#
# 방법 1
# t = int(input())
# for tc in range(1, t + 1):
#     array = []
#     n = input().rstrip()
#     array.extend(n)
#
#     a = array[:len(array) // 2]
#     b = array[-1: -(len(array) // 2) - 1:-1]
#     if a == b:
#         print(f"#{tc} 1")
#     else:
#         print(f"#{tc} 0")


'''
10
level
samsung
eye
exo
ioi
blackpink
hannah
B1A4
linetown
nursesrun
'''

# 방법 2
k = int(input())
for tc in range(1, k+1):
    s = input()
    # print(s)
    # print(s[::-1])
    if s == s[::-1]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")