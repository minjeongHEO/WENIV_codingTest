# 상하좌우 - 구현
n = int(input())
plans = list(map(str, input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
# x = 1
# y = 1
x, y = 1, 1

move_type = ["L", "R", "U", "D"]


for plan in plans:

    for m in range(len(move_type)):
        if plan == move_type[m]:
            nx = x + dx[m]
            ny = y + dy[m]

    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(f"{x} {y}")

'''
5
R R R U D D
'''
