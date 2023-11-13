# 쉬운 거스름돈

for tc in range(1,int(input())+1):
    change = [50000,10000,5000,1000,500,100,50,10]
    result = []
    n = int(input())

    for i in range(8):
        result.append(n // change[i])
        n -= change[i] * (n // change[i])

    print(f"#{tc}")
    print(*result)
'''
58,532 kb
메모리
142 ms
실행시간
'''

# ========================================================
# 다른 풀이
# ========================================================
for t in range(int(input())):
    n = int(input())
    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{t+1}')
    for c in coin:
        print(n//c, end=' ')
        n = n % c
    print()
'''
42,184 kb
메모리
94 ms
실행시간
'''