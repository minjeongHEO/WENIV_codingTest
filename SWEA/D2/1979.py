# 어디에 단어가 들어갈 수 있을까 - 구현 및 시뮬레이션

for tc in range(1, int(input())+1):
    result = 0
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    # 가로 확인
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[i][j] == 1:
                cnt += 1
            if data[i][j] == 0 or j == n-1: # 끝까지 왔다면
                if cnt == k: # 카운트가 다 세졌으면 단어가 들어갈 수 있는 것
                    result += 1
                if data[i][j] == 0:
                    cnt = 0

    # 세로 확인
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[j][i] == 1:
                cnt += 1
            if data[j][i] == 0 or j == n - 1:  # 끝까지 왔다면
                if cnt == k:  # 카운트가 다 세졌으면 단어가 들어갈 수 있는 것
                    result += 1
                if data[j][i] == 0:
                    cnt = 0

    print(f"#{tc} {result}")

