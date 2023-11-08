# 지그재그 숫자
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    odd = 0
    add = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            add += i
        else:
            odd += i

    print('#{} {}'.format(tc, odd-add))