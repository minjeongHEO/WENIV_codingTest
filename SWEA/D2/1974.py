# 스도쿠 검증
# 가로 한줄씩 점검 set에 넣고 길이가 9
# 3x3 네모 9번 점검해서 set에 넣고 길이가 9

spot = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

for tc in range(1, int(input())+1):
    graph = [list(map(int, input().split())) for _ in range(9)]
    row_check = True
    col_check = True
    box_check = False
    result = 0
    # 가로 줄 점검 (행)
    for i in graph:
        s = set(i)
        # print(i)
        # print(s)
        # print(len(s))
        if len(s) != 9:
            row_check = False
            break
    # 세로 줄 점검 (열)
    if row_check:
        for i in range(9):
            s = set()
            for j in range(9):
                s.add(graph[j][i])
            if len(s) != 9:
                col_check = False
                break

    # print(spot)
    # print(spot[0]) #(0, 0)
    #2. 3x3 네모 9번 점검해서 set에 넣고 길이가 9
    if row_check and col_check:
        for i in range(9):
            # x = spot[i][0]
            # y = spot[i][1]
            x, y = spot[i]
            # test = set([])

            test = set(graph[x + j][y + k] for j in range(3) for k in range(3))

            # for j in range(3):
            #     for k in range(3):
            #         test.add(graph[x+j][y+k])

            if len(test) != 9:
                box_check = False
                break
            else:
                box_check = True

    if box_check:
        result = 1

    print(f"#{tc} {result}")
'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''
# =====================================================================
# 튜플리스트(spot) 안쓰고 구하는법
# =====================================================================
for tc in range(1, int(input())+1):
    graph = [list(map(int, input().split())) for _ in range(9)]
    row_check = True
    col_check = True
    box_check = False
    result = 0
    # 가로 줄 점검 (행)
    for i in graph:
        s = set(i)
        # print(i)
        # print(s)
        # print(len(s))
        if len(s) != 9:
            row_check = False
            break
    # 세로 줄 점검 (열)
    if row_check:
        for i in range(9):
            s = set()
            for j in range(9):
                s.add(graph[j][i])
            if len(s) != 9:
                col_check = False
                break

    # print(spot)
    # print(spot[0]) #(0, 0)
    #2. 3x3 네모 9번 점검해서 set에 넣고 길이가 9
    if row_check and col_check:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                test = set(graph[i + x][j + y] for x in range(3) for y in range(3))
                if len(test) != 9:
                    box_check = False
                    break
                else:
                    box_check = True

    if box_check:
        result = 1

    print(f"#{tc} {result}")

