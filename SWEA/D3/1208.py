# [S/W 문제해결 기본] 1일차 - Flatten
#
for tc in range(1, 11):
    n = int(input())
    tower = list(map(int, input().split()))

    for i in range(n):
        max_idx = tower.index(max(tower))
        min_idx = tower.index(min(tower))

        tower[max_idx] -= 1
        tower[min_idx] += 1

        if max(tower) == min(tower):
            break

    print(f"#{tc} {max(tower) - min(tower)}")
'''
62,540 kb
메모리
184 ms
실행시간
'''

# ==========================================================
# 실패 코드
#  덤프 작업 후의 최대값과 최소값 간의 차이가 아닌, 마지막 덤프 작업 이전의 최대값과 최소값 간의 차이를 출력하게 됩니다.
# 문제를 해결하려면, 덤프 작업이 모두 완료된 후에 최대값과 최소값을 다시 계산해야 합니다.
# ==========================================================
# for tc in range(1, 11):
#     n = int(input())
#     tower = list(map(int, input().split()))
#     max_val = 0
#     min_val = 0
#     for i in range(n):
#         max_val = max(tower)
#         min_val = min(tower)
#         tower[tower.index(max_val)] -= 1
#         tower[tower.index(min_val)] += 1
#
#         if max_val == min_val:
#             break
#
#     print(f"#{tc} {max_val-min_val}")

# ---------------------------------------------------
# 수정 코드
# ---------------------------------------------------
# [S/W 문제해결 기본] 1일차 - Flatten

for tc in range(1, 11):
    n = int(input())
    tower = list(map(int, input().split()))

    for i in range(n):
        max_val = max(tower)
        min_val = min(tower)
        tower[tower.index(max_val)] -= 1
        tower[tower.index(min_val)] += 1

        if max_val == min_val:
            break

    max_val = max(tower)
    min_val = min(tower)

    print(f"#{tc} {max_val-min_val}")
'''
62,012 kb
메모리
191 ms
실행시간
'''