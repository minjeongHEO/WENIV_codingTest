# 게임 개발 - 구현 (전형적인 시뮬레이션 문제)
# 첫쨰줄
# 세로 x 가로
#  n  x  m (3 ~ 50)
#
# # 둘쨰줄
# 캐릭터의 좌표 a,b / 방향 d (3서 2남 1동 0북)
#
# # 셋쨰줄 ~ n번
# 육지 와 바다 출력
# 0       1

# MAX = 50+10
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

N_MAX = n+2
M_MAX = m+2
graph = [[1]*M_MAX for _ in range(N_MAX)]
visited = [[False]*M_MAX for _ in range(N_MAX)]
visited[x][y] = True

print(graph)
# 루프돌면서 graph에 입력 받는다
for i in range(n):
    input_arr = list(map(int, input().split()))
    for j in range(m):
        graph[i+1][j+1] = input_arr[j]
print(graph)
#
# 현재위치에서 방향을 기준으로 반시계방향으로 차례대로 갈곳을 정한다
#
# 1. 왼쪽에 가보지않은 칸 존재 => 왼쪽 방향으로 회전 + 왼쪽으로 한칸 전진
# 2. 왼쪽에 가보지않은 칸 미존재 => 왼쪽 방향으로 회전만 + 1번로직 또 수행
# 3. 만약 네 방향 모두 가본칸or바다칸 => 방향은 유지한채 한칸뒤로 + 1번로직 또 수행

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전 (반시계방향으로 ?) (3서 2남 1동 0북)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]

    #회전하고 정면에 가보지 않은 칸이 존재하면 이동하기
    if not visited[nx][ny] and graph[nx][ny] == 0:
        visited[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: #회전하고 정면에 가본칸 or 바다
        turn_time += 1

    #네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 방향은 유지한채 한칸 뒤로
        nx = x - dx[direction]
        ny = y - dx[direction]

        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:#뒤에 바다로 막혀있어서 못가는 경우
            break

        turn_time = 0

print(count)


'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
