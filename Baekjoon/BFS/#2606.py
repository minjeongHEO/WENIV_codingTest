# 바이러스 - 2606
from collections import deque
n = int(input()) # 노드의 수
m = int(input()) # 연결된 쌍의 수

visited = [False] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

count = 0
def bfs(v):
    queue = deque([v]);
    visited[v] = True
    # cur = queue.popleft() #popleft()는 while문 안에!!
    global count

    while queue:
        cur = queue.popleft()
        for i in range(1, n+1):
            # if graph[v][i] == 1 and not visited[i]:
            if not visited[i] and graph[cur][i] == 1:
                count += 1
                visited[i] = True
                queue.append(i)

bfs(1) #여기에 1을 지정하여 실행했기에 1번에 연결된 컴퓨터만 센다.
print(count)