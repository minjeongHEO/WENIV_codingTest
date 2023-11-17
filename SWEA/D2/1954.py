# 달팽이 숫자
# 1 ~ n*n

# ===================================================================
# 1. DFS 방식
# ===================================================================
# for tc in range(1, int(input())+1):
#     #  0     1     2     3
#     # [우측, 아래, 좌측, 위에]반복
#     nx = [0, 1, 0, -1] #행 세로
#     ny = [1, 0, -1, 0] #열 가로
#
#     n = int(input())
#
#     graph = [[0]*n for _ in range(n)]
#     visited = [[False]*n for _ in range(n)]
#
#     def dfs(x,y,loc,num):
#         visited[x][y] = True
#         graph[x][y] = num
#
#         for i in range(4):
#             _X = x + nx[loc]
#             _Y = y + ny[loc]
#
#             if 0 <= _X < n and 0 <= _Y < n and not visited[_X][_Y]:
#                 dfs(_X, _Y, loc, num+1)
#                 return
#                 '''
#                 return 키워드는 함수의 실행을 즉시 중단하고, 함수를 호출한 위치로 돌아가게 합니다. 따라서 return 키워드를 만나면 현재 실행 중인 함수가 종료되며, 이 경우 for 반복문도 함께 종료됩니다.
#                 이 코드에서 return은 새로운 위치(_X, _Y)로의 이동이 성공적으로 이루어진 경우, 즉, 새로운 위치가 그래프의 범위 내에 있고 아직 방문하지 않은 경우에 호출됩니다. 이 경우에는 더 이상 현재 방향(loc)에서의 다른 위치를 체크할 필요가 없으므로, return을 통해 함수를 종료하고, 새로운 위치에서 다시 dfs 함수를 시작합니다.
#                 '''
#             else:
#                 loc = (loc + 1) % 4
#                 '''
#                 0 => 1
#                 1 => 2
#                 2 => 3
#                 3 => 0
#                 '''
#
#         #여기는 else 로직을 탔을 때 실행되는 부분
#         _X = x + nx[loc]
#         _Y = y + ny[loc]
#         if 0 <= _X < n and 0 <= _Y < n and not visited[_X][_Y]:
#             dfs(_X, _Y, loc, num+1)
#
#     dfs(0,0,0,1)
#
#     print(f"#{tc}")
#     for i in range(n):
#         for j in range(n):
#             print(graph[i][j], end=" ")
#         print()

# ===================================================================
# 2. 다른 풀이 (while문 방식)
# ===================================================================
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for t in range(1, int(input()) + 1):
    n = int(input())
    result = [[0] * n for _ in range(n)]
    cnt, i = 1, 0
    x, y = 0, 0
    result[0][0] = cnt
    while 1:
        if cnt == n ** 2:
            break
        cnt += 1
        x += dx[i]
        y += dy[i]
        if 0 <= x < n and 0 <= y < n and result[x][y] == 0:
            result[x][y] = cnt
        else:
            x -= dx[i]
            y -= dy[i]
            cnt -= 1
            i = (i + 1) % 4
    print(f"#{t}")
    for i in result:
        print(*i)

'''
DFS 방식: 이 방법은 재귀적인 방식으로 문제를 해결합니다. DFS는 깊이 우선 탐색으로, 현재 위치에서 가능한 한 깊게 탐색하고 더 이상 탐색할 곳이 없을 때 이전 위치로 돌아가는 방식입니다.
            이 방법은 코드가 간결하고 이해하기 쉽지만, 깊이가 너무 깊어지면 스택 오버플로우가 발생할 수 있습니다.
while문 방식: 이 방법은 반복문을 이용하여 문제를 해결합니다. 이 방법은 DFS보다 코드가 조금 더 복잡하지만, 깊이에 관계없이 안정적으로 실행됩니다.

따라서, 어느 방법이 더 효율적인지는 문제의 상황과 요구사항에 따라 다릅니다. 예를 들어, 달팽이가 이동해야 하는 칸의 수(n)가 매우 큰 경우에는 while문 방식이 더 효율적일 수 있습니다. 반면, n이 작은 경우에는 DFS 방식이 코드가 더 간결하고 이해하기 쉬울 수 있습니다.
'''

# =====================================================================
# dfs 방법 2(visted 따로 배열 안만들고)
# =====================================================================
# 우, 하, 좌, 상 순서로 이동
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 테스트 케이스 개수만큼 반복
for tc in range(1, int(input())+1):
    dir = 0  # 이동 방향 초기화
    num = 0  # 채워질 숫자 초기화
    n = int(input())  # 달팽이 배열의 크기 입력 받기
    graph = [[0]*n for _ in range(n)]  # n*n 크기의 달팽이 배열 초기화

    print(f"#{tc}")  # 테스트 케이스 번호 출력

    # DFS 함수 정의
    def dfs(x, y):
        global num
        global dir

        # x, y가 배열 범위 내에 있고, 아직 방문하지 않은 경우
        if -1 < x < n and -1 < y < n and graph[x][y] == 0:
            num += 1
            graph[x][y] = num
            nx = x + move[dir % 4][0]
            ny = y + move[dir % 4][1]
            dfs(nx, ny)  # 다음 위치로 이동
            return

        # x, y가 배열 범위를 벗어나거나, 이미 방문한 경우
        else:
            dir += 1  # 방향 변경
            nx = x + move[dir % 4][0]
            ny = y + move[dir % 4][1]
            if -1 < nx < n and -1 < ny < n:  # 다음 위치가 배열 범위 내에 있는 경우에만 재귀 호출
                dfs(nx, ny)  # 다음 위치로 이동
                return
    # DFS 시작
    dfs(0, 0)

    # 결과 출력
    for i in graph:
        print(*i)

'''
 재귀 함수에서 'return'은 해당 재귀 호출을 종료하고, 이전의 호출 상태로 돌아가는 역할을 합니다. 
 따라서 재귀 함수에서 'return'을 적절히 사용하면 
 불필요한 재귀 호출을 줄이고, 런타임 에러를 방지하는 데 도움이 됩니다.
'''