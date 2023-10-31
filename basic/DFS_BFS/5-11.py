# 이코테 문제 5-11) 미로 탈출
# BFS
from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append((list(map(int, input()))))


print(graph)

# 이동할 네 방향 정의 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    # 덱라이브러리 써서 큐 구현
    queue = deque()

    queue.append((x,y))

    #큐가 빈 상태일 때까지 반복한다
    while queue:
        x,y = queue.popleft()

        #현재 위치에서 네 방향(상하좌우)으로의 위치 확인
        for i in range(4): # 0 1 2 3
            nx = x + dx[i]
            ny = x + dx[i]

            #이동했는데 미로 공간을 벗어나는 경우 예외처리
            if nx < 0 or nx >=n or ny <0 or ny >= m:
                continue
            #이동못하는 경우, 막힌경우
            if graph[nx][ny] == 0:
                continue

            #이동된 경우 + 처음 방문하는 곳인 경우 에 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


print(bfs(0,0))

'''
5 6
101010
111111
000001
111111
111111
'''
'''
3 3
110
010
011
'''
