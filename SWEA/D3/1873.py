# 상호의 배틀필드

# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# arrow = ["^", "v", "<", ">"]
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)
#
# dir = ["U", "D", "L", "R" , "S"]
# U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
# 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진한다.
# 부딪힌 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지가 된다

# start_x = 0
# start_y = 0
# my_arw = "^"
# graph = []
# field = [".", "*", "#", "-"]
# arrow = ["^", "v", "<", ">"]
# dir = ["U", "D", "L", "R", "S"]
#
# def battle(d, x, y, my_arw):
#     global start_x,start_y
#
#     if dir.index(d) != 4:
#         graph[x][y] = arrow[dir.index(d)]
#         #한칸 위의 칸이 평지라면
#         if dir.index(d) == 0:
#             if graph[x-1][[y]] == field[0]:
#                 start_x = x-1
#         #한칸 아래 칸이 평지라면
#         elif dir.index(d) == 1:
#             if graph[x + 1][[y]] == field[0]:
#                 start_x = x + 1
#         #한칸 왼쪽 칸이 평지라면
#         elif dir.index(d) == 2:
#             if graph[x][[y - 1]] == field[0]:
#                 start_y = y - 1
#         #한칸 오른쪽 칸이 평지라면
#         elif dir.index(d) == 3:
#             if graph[x][[y + 1]] == field[0]:
#                 start_y = y + 1
#     else:
#
#
# for tc in range(1, int(input())+1):
#     # 높이가 H, 너비가 W
#     h, w = map(int, input().split())
#     graph = [['-']*w for _ in range(h)]
#
#     for i in range(h):
#         str = list(input())
#         for idx,j in enumerate(str): #w
#             graph[i][idx] = j
#
#     print(graph)
#
#     n = int(input()) # 사용자가 넣을 입력의 개수
#     my_dir = list(input()) # 길이가 N인 문자열
#
#     for ar in arrow:
#         for i_idx, i in enumerate(graph):
#             if ar in i:
#                 start_x = i_idx
#                 start_y = i.index(ar)
#                 my_arw = ar
#
#     for i in my_dir: # SURSSSSUSLSRSSSURRDSRDS
#         battle(i, start_x, start_y, my_arw)

# ====================================================
# 수정
# ====================================================
dir = ['U', 'D', 'L', 'R', 'S']
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # U, D, L, R에 대응되는 좌표 이동
tank = ['^', 'v', '<', '>']

def battle(d, x, y):
    global start_x,start_y, my_arw

    if d != 'S':
        idx = dir.index(d)
        # 탱크 방향을 바꿔줍니다
        my_arw = tank[idx]
        graph[x][y] = my_arw
        nx, ny = x + dx[idx], y + dy[idx]
        # 한 칸 전진하는 경우, 평지라면 이동
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == '.':
            graph[x][y], graph[nx][ny] = '.', my_arw
            start_x, start_y = nx, ny
    else:
        # S인 경우, 총알을 발사
        idx = tank.index(my_arw)
        nx, ny = x + dx[idx], y + dy[idx]
        while 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == '#':
                break
            elif graph[nx][ny] == '*':
                graph[nx][ny] = '.'
                break
            nx, ny = nx + dx[idx], ny + dy[idx]

for tc in range(1, int(input())+1):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    n = int(input()) 
    my_dir = list(input()) 

    # 탱크의 초기 위치와 방향을 찾습니다
    for i in range(h):
        for j in range(w):
            if graph[i][j] in tank:
                start_x, start_y = i, j
                my_arw = graph[i][j]

    for d in my_dir:
        battle(d, start_x, start_y)

    print(f'#{tc}', end=" ")
    for row in graph:
        print(''.join(row))

'''
63,828 kb
메모리
269 ms
실행시간
'''
        
# ====================================================
# 다른 코드
# ====================================================
move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

command_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4,
                '^': 0, 'v': 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2: '<', 3: '>'}

serch_list = ['<', '>', '^', 'v']

for t in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    map_list = [list(input()) for _ in range(H)]
    # 탱크의 위치를 찾는다.
    for i in range(H):
        for j in range(W):
            if map_list[i][j] in serch_list:
                tank_pos = (i, j, command_dict[map_list[i][j]])
                break
        # 브레이크에 안걸렸다면 진행한다.
        else:
            continue
        # 브레이크가 걸렸다면 모든 반복문을 나온다.
        break
    # N값은 안쓰니까 버린다.
    input()
    # 명령어 저장
    commands = input()
    # 명령어를 순회하면서 처리
    for command in commands:
        temp = command_dict[command]
        # 포탄 발싸라면
        if temp == 4:
            # 탱크 위치에서 탱크가 바라보는 방향의 위치를 얻는다.
            dy = tank_pos[0]
            dx = tank_pos[1]
            # 포탄은 계속 전진한다.
            while True:
                dy += move_list[tank_pos[2]][0]
                dx += move_list[tank_pos[2]][1]
                # 포탄이 밖으로 벋어나거나 강철벽을 만나면 아무처리도 안한다.
                if 0 > dy or dy >= H or 0 > dx or dx >= W or map_list[dy][dx] == '#':
                    break
                # 돌벽을 만나게 된다면
                if map_list[dy][dx] == '*':
                    # 평지로 바꿔준다.
                    map_list[dy][dx] = '.'
                    break
        # 이동 명령이라면
        else:
            y = tank_pos[0]
            x = tank_pos[1]
            dy = y + move_list[temp][0]
            dx = x + move_list[temp][1]
            map_list[y][x] = command_dict[temp]
            tank_pos = (y, x, temp)
            # 맵 범위 안에있고 평지여야함.
            if 0 <= dy < H and 0 <= dx < W and map_list[dy][dx] == '.':
                # 기존위치를 평지로 바꾸고
                map_list[y][x] = '.'
                # 가야하는 위치에 탱크 표시
                map_list[dy][dx] = command_dict[temp]
                # 탱크위치 갱신
                tank_pos = (dy, dx, temp)
    print('#{}'.format(t), end=' ')
    for m in map_list:
        print(''.join(m))

'''
63,832 kb
메모리
271 ms
실행시간
'''