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

print(graph)


def solution(x,y):
    count = 0

    # 예외 처리
    if x >= m or y >= n:
        return False

    # -이면 x축으로 확인
    if graph[x][y] == '-':
        graph[x][y] = ''
        solution(x, y + 1)
    else:
        return True

    # |이면 y축으로 확인
    if graph[x][y] == '|':
        graph[x][y] = ''
        solution(x+1, y)
    else:
        return True

    if graph[x][y] == '':
        return False

count = 0
for i in range(n):
    for j in range(m):
        # if solution(i,j) == True:
        #     continue
        # else:
        #     count += 1
        #
        if solution(i,j) == False:
            continue
        elif solution(i,j) == True:
            count += 1

print(count)
print(graph)
