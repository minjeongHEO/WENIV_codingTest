# 그리디 - 숫자 카드 게임
# n = 행 세로
# m = 열 가로
#
# 먼저 뽑고자 하는 카드가 포함된 행을 선택한다.
#
# 그다음 그 행에 포함된 카드들 중 숫자가 낮은 숫자 뽑는다
#
# 즉 처음 카드를 골라낼 행을 선택할 때
# 이후에 해당 행에서 가장 숫자가 작은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수있도록 전략을 세운다

import sys

n, m = map(int, input().split())
#
# n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, input().split())) for i in range(n)]
#
# graph = []
# for _ in range(n):
#     row = list(map(int, sys.stdin.readline().rstrip().split()))
#     graph.append(row)

print(graph)
value = 0
for i in range(n):
    print(graph[i])

    if value < min(graph[i]):
        value = min(graph[i])
    else:
        continue

print(value)

'''
3 3
3 1 2
4 1 4
2 2 2
'''
'''
2 4
7 4 1 8
3 3 3 4
'''
# ================== graph 에 안넣고 확인하기 ======================
n, m = map(int, input().split())
result = 0
#한 줄씩 입력받으면서 확인하기
for i in range (n):
    data = list(map(int , input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)

    result = max(result, min_value)
    # 코드는 각 행의 최소값(min_value)과 이전 행까지의 최소값들 중에서
    # 가장 큰 값(result)을 비교해서,
    # 더 큰 값을 result에 저장하는 코드입니다.

print(result)