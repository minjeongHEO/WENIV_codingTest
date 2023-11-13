# 간단한 압축 풀기

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = ""
    print(f"#{tc}")

    for i in range(n):
        # 알파벳, 숫자
        Ci, Ki = map(str, input().split())
        Ki = int(Ki)

        # Ci문자 Ki번 생성
        for j in range(Ki):
            result += Ci

            if len(result) == 10:
                print(result)
                result = ""

        # 마지막이라면 10자 아니어도 그냥 출력
        if i == n-1:
            print(result)
'''
58,788 kb
메모리
160 ms
실행시간
'''

# =====================================================================
# 다른 풀이
# =====================================================================
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = ""

    for i in range(N):
        C, K = input().split()
        result += C * int(K)

    print("#{0}".format(tc))
    for i in range(0, len(result), 10):
        print(result[i:i + 10])
# =====================================================================
'''
43,256 kb
메모리
98 ms
실행시간
'''

