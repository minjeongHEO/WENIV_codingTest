# DFS와 BFS
'''
정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
정점의 개수  = 행 = n / 정점 번호는 1번부터 N번
간선의 개수 = m
탐색을 시작할 정점번호 = v

노드를 4개 받으면
graph

'''
from collections import deque
n,m,v = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(m)]
# graph = n+1 * n+1 인 2차원 배열이니까 기본값을 False로 설정해놓자
graph = [[False] * (n+1) for _ in range(n+1)]
'''
N이 아니라 N+1을 하는 이유??
N이 4일 때, graph는 5x5로 만들어야지 인덱스가 0~4 x 0~4로 만들어지기 때문이에요~
이렇게하면 0번 인덱스 위치는 사용하지 않아서 낭비(?)되는 것일 수도 있지만, 
이후에는 인덱스를 접근할 때 index - 1로 접근하지 않고 index로 바로 접근할 수 있어서 골치 아픈 인덱스 계산을 더 간소화할 수 있어요!
'''
# visited 배열은 1차원 배열
visited = [False] * (n+1)
# visited = [[0]*2 for _ in range(m)]

# 1. graph정보 입력
for _ in range(m):
    a,b = map(int, input().split())

    graph[a][b] = True
    graph[b][a] = True # !!!반대의 경우도 True로 넣어줘야함


#1.DFS
def dfs(v):
    visited[v] = True  # 해당 V값 방문처리

    print(v, end=' ')

    for next in range(1, n+1):
        if not visited[next] and graph[v][next]:  # 만약 next값을 방문하지 않았고 v와 연결이 되어 있다면
            dfs(next) #해당 i값으로 재귀함수 호출



#2.BFS
def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for next in range(1, n+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


dfs(v)
print()

#visited 배열 초기화
visited = [False] * (n+1)
bfs(v)

