# 수도 요금 경쟁

t = int(input())

for tc in range(1,t+1):
    p, q, r, s, w = map(int,input().split())
    # price = []
    price = [(w * p)] #a회사

    if w > r:
        price.append(q + (w-r)*s)
    else:
        price.append(q)

    print('#{} {}'.format(tc, min(price)))
    # A = P * W
    # B = Q if W <= R else Q + (W - R) * S
    # print(f"#{test_case} {min(A, B)}")