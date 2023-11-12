# 파스칼의 삼각형
for tc in range(1,int(input())+1):
    n = int(input())
    arr = [[0]*(n+1) for _ in range(n+1)]
    print(arr)

    for i in range(1,n+1): #1~4 1

        for j in range(i): #0 1 2 3 j= 0
            if j == 0 or j == i-1:
                val = 1
            else:
                val = arr[i-1][j-1] + arr[i-1][j]

            arr[i][j] = val


    print(f"#{tc}")
    for index,i in enumerate(arr):
        if index == 0:
            continue
        else:
            print(*i[:index])
