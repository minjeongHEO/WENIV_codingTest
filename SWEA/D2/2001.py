# 파리 퇴치 - 완전 탐색

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    # n x n 박스크기
    # 파리채는 m x m
    arr = [list(map(int, input().split())) for _ in range(n)]
    # kill = set([])

    kill = []
    # dx = [0, 0, 1, -1] #행 세로
    # dy = [1, -1, 0, 0] #열 가로
    # x,y = 0,0

    # 파리채를 내려칠 곳 탐색
    for i in range(n-m+1): #행
        for j in range(n-m+1): #열
            fly = 0

            # 해당 위치를 타격했을 때 잡을 수 있는 파리의 수 탐색
            for k in range(m):
                for l in range(m):
                    fly += arr[i + k][j + l]

            kill.append(fly)
    # 배열 범위 안에서 가능한 경우의 수 중에서 가장 많은 파리를 잡을 때의 수 출력
    print("#" + str(tc), max(kill))


'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''

