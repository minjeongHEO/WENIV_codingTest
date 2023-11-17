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
'''
58,796 kb
메모리
171 ms
실행시간
'''
# ======================================================================
# 다른 풀이
# ======================================================================
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split())) #n 7
    b = list(map(int, input().split())) #m 6

    multiple = []

    if m>n:
        for i in range(m-n+1):
            sum = 0
            for j in range(n):
                sum += a[j] * b[j+i]

            multiple.append(sum)
    else:
        for i in range(n-m + 1):
            sum = 0
            for j in range(m):
                sum += a[j + i] * b[j]

            multiple.append(sum)

    print(f"#{tc} {max(multiple)}")
'''
58,264 kb
메모리
159 ms
실행시간
'''
