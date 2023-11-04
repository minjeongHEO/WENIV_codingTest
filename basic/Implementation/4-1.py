# 상하좌우 - 구현
n = int(input())
arrow = list(map(str, input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
x = 1
y = 1
for i in arrow:
    # dx[0]    dy[0] (0,-1) 왼 L
    # dx[1]    dy[1] (0,1) 오 R
    # dx[2]    dy[2] (-1,0) 위 U
    # dx[3]    dy[3] (1,0) 아래 D
    if i == 'L':
        if x + dx[0] > 0 and x + dx[0] <= n and y + dy[0] > 0 and y + dy[0] <= n:
            x += dx[0]
            y += dy[0]
        else:
            continue
    elif i == 'R':
        if x + dx[1] > 0 and x + dx[1] <= n and y + dy[1] > 0 and y + dy[1] <= n:
            x += dx[1]
            y += dy[1]
        else:
            continue
    elif i == 'U':
        if x + dx[2] > 0 and x + dx[2] <= n and y + dy[2] > 0 and y + dy[2] <= n:
            x += dx[2]
            y += dy[2]
        else:
            continue
    elif i == 'D':
        if x + dx[3] > 0 and x + dx[3] <= n and y + dy[3] > 0 and y + dy[3] <= n:
            x += dx[3]
            y += dy[3]
        else:
            continue

print(f"{x} {y}")

'''
5
R R R U D D
'''