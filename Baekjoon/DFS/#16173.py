# 점프왕 쩰리 (Small)
'''
가로와 세로의 칸 수가 같은 정사각형의 구역 내부 (넘으면 패배)
항상 출발은 (1,1)에서 시작
이동은 오른쪽. 아래 두가지만 가능
쩰리가 가장 오른쪽,맨아래에 도착 시 그 즉시 쩰리의 승리
쩰리는 현재 밟고 있는 칸의 수 만큼 이동가능
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
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    해당위치값 = graph[x][y]
    if x == n-1 and y == n-1:
        print('HaruHaru')
        return 'HaruHaru'

    for i in range(2):
        if i==0:
            if x+해당위치값 > n-1:
                continue
            else:
                dfs(x+해당위치값, y)
                break

        if i == 1:
            if y+해당위치값 > n-1:
                print('Hing')
                return 'Hing'
            else:
                dfs(x,y+해당위치값)
                break


dfs(0, 0)


