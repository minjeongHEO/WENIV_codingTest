# [S/W 문제해결 기본] 2일차 - Sum

for _ in range(10):
    n = int(input())

    # graph = [list(map(int, input().split())) for _ in range(100)]
    graph = [list(map(int, input().split())) for _ in range(5)]
    s = set([])

    d1 = 0
    d2 = 0
    # for i in range(100):
    for i in range(5):
        row = 0
        col = 0
        # d2 += graph[i][99-i]
        d2 += graph[i][4-i]
        # for j in range(100):
        for j in range(5):
            row += graph[i][j]
            col += graph[j][i]
            if i==j:
                d1 += graph[i][j]

        s.add(row)
        s.add(col)

    s.add(d1)
    s.add(d2)

    print(f"#{n} {max(s)}")

'''
1
4 4 3 2 1
2 2 1 6 5
3 5 4 6 7
4 2 5 9 7
8 1 9 5 6
'''