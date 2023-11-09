# 두 개의 숫자열

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    result = -float('inf') #음수 무한대(negative infinity)

    if n > m:
        big = n
        small = m
        a = list(map(int, input().split())) # a가 큰거
        b = list(map(int, input().split())) # b가 작은거
    else:
        big = m
        small = n
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))

    for i in range(big - small + 1): #1을 더하는 이유는 a의 시작점을 정해야하므로
        max = 0
        for j in range(small):
            max += b[j] * a[j + i] #여기서 i를 더한다.

        if max > result: # max값을 전max값과 비교후 더 크면 result값에 업데이트
            result = max

    print(f'#{tc} {result}')

