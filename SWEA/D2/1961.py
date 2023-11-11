# 숫자 배열 회전

for tc in range(1, int(input())+1):
    array_90 = []
    array_180 = []
    array_270 = []

    n = int(input())

    data = [list(map(int, input().split())) for _ in range(n)]


    # 90
    for i in range(n): #열
        num = ''
        for j in range(n-1,-1,-1): #행
            num += str(data[j][i])

        array_90.append(num)

    # 180
    for i in range(n-1,-1,-1): #행
        num = ''
        for j in range(n-1,-1,-1): #열
            num += str(data[i][j])

        array_180.append(num)

    # 270
    for i in range(n-1,-1,-1): #열
        num = ''
        for j in range(n): #행
            num += str(data[j][i])

        array_270.append(num)

    print(f"#{tc}")

    for i in range(n):
        print(f"{array_90[i]} {array_180[i]} {array_270[i]}")

'''
2
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
'''