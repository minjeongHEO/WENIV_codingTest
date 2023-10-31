'''
- 세로 크기N / 가로 크기 M
- 나무판자의 크기
1의너비
양수의 길이를

- 기훈이 방은
직사각형 모양
방 안에는 벽 ,  평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다.

두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자
두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

바닥을 장식하는데 필요한 나무판자의 개수를 출력하라
'''
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(str, input())))
    # graph.append(list(input()))

def solution(x,y):
    # 예외 처리
    if x >= m or y >= n:
        return False

    # 바닥 장식 모양이 '-' 일 때
    if graph[x][y] == '-':
        graph[x][y] = 1  # 해당 노드 방문처리
        for _y in [1, -1]:  # 양옆(좌우) 확인하기
            Y = y + _y
            # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                solution(x, Y)

    # 바닥 장식 모양이 '|' 일 때
    if graph[x][y] == '|':
        graph[x][y] = 1 # 해당노드 방문처리
        for _x in [1, -1]:  # 위아래(상하)확인하기
            X = x + _x
            # 상하노드가 주어진 범위를 벗어나지 않고, '-' 모양이라면, 재귀함수 호출
            if (X > 0 and X < n) and graph[X][y] == '|':
                solution(X, y)
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            solution(i, j)  # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
            count += 1

print(count)
