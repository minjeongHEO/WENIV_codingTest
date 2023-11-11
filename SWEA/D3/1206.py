# [S/W 문제해결 기본] 1일차 - View

# dfs로 풀면 될꺼깥은데 = > 아님
# 깊이 우선 탐색(DFS)보다는 각 건물의 높이를 순차적으로 비교하면서 문제를 해결하는 것이 더 적합합니다.
# 이 문제의 경우 각 건물이 서로 연결되어 있지 않고, 주변 건물의 높이에 따라 조망권이 결정되므로 DFS를 사용하기 어렵습니다.

for test_case in range(1,11):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    for i in range(2, n-2):
        # 먼저 양옆 건물의 높이를 확인하고
        left_best = max(buildings[i-1], buildings[i-2])
        right_best = max(buildings[i+1], buildings[i+2])
        best = max(left_best, right_best)

        if buildings[i] > best: #만약 내 건물의 높이보다 낮다면 현재 위치는 조망권 층수가 있다.
            result += buildings[i] - best

    print(f"#{test_case} {result}")