# 점프왕 쩰리 (Small)
'''
가로와 세로의 칸 수가 같은 정사각형의 구역 내부 (넘으면 패배)
항상 출발은 (1,1)에서 시작
이동은 오른쪽. 아래 두가지만 가능
쩰리가 가장 오른쪽,맨아래에 도착 시 그 즉시 쩰리의 승리
쩰리는 현재 밟고 있는 칸의 수 만큼 이동가능

3
1 1 10
1 5 1
2 2 -1

HaruHaru

3
2 2 1
2 2 2
1 2 -1

Hing
'''

#예외 처리
# n < 2 or n >3
# return false
#

#
#
# 이동은 아래 또는 오른쪽
# graph[x+1][y] : 아래
# graph[x][y+1] : 오른쪽
#
# 근데 밟은만큼 이동할수있자나
# 해당위치값 = graph[x][y]
# graph[x+해당위치값][y] : 아래
# graph[x][y+해당위치값] : 오른쪽
#
# # for _y in [1, -1]:  # 양옆(좌우) 확인하기
# HaruHaru
#
# Hing
#
# 해당 위치가  graph[n-1][n-1]이 결국 나오면 HaruHaru
#
# 만약
# 해당 위치가 graph[x][y]라고 했을 때
# x > n-1
# or
# y > n-1
# 이면 Hing

n = int(input())

# ******** 게임판의 구역을 입력받는다. 2차원 리스트 ********
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

graph = [list(map(int, input().split())) for _ in range(n)]

# ******** 방문여부를 저장할 visit 2차원 리스트를 만든다. ********
# visit = []
# n = 3
# for i in range(n):       # i = 0, 1, 2
#     row = [0]*n          # row = [0, 0, 0]
#     visit.append(row)
#
# print(visit)             # visit = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

visited = [[0]*n for _ in range(n)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]




def dfs(x, y):
    visited[x][y] = True # 방문여부체크!!!!!!!

    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            dfs(nx, ny)



dfs(0, 0)

if visited[n-1][n-1] == True:
    print('HaruHaru')
else:
    print('Hing')




