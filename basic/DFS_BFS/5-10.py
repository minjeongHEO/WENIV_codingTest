# 이코테 문제 5-10) 음료수 얼려먹기
# DFS
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

def solution(x,y):
    # 범위를 벗어나는 거 예외처리
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] == 0:
        # 방문처리하고
        graph[x][y] = 1
        # 상 하 좌 우 도 재귀호출
        solution(x-1, y)
        solution(x, y-1)
        solution(x+1, y)
        solution(x, y+1)

        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if solution(i,j) == True:
            result += 1

print(result)


# 입력 예시
'''
4 5
00110
00011
11111
00000
'''

# ==================================================================
# 다른 풀이
# ==================================================================
dir = [(-1,0),(1,0),(0,-1),(0,1)]

n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
count = 0

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m or graph[x][y] != 0:
        return False
    graph[x][y] = 1
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        dfs(nx,ny)
    return True

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)