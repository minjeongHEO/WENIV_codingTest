# [S/W 문제해결 응용] 2일차 - 최대 상금

# 숫자를 배열에 넣고 extend

# t = int(input())
# for tc in range(1,t+1):
#     number, change = map(int, input().split())
#     arr = []
#     arr.extend(str(number))
#
#     print(f"-------------{arr}-------------")
#     max_num = 0
#     for _ in range(change):
#         print(max(arr))
#         print(arr.index(max(arr)))

# ===============================================================
# 완전탐색 해서 값들을 set에 넣어 중복을 제거하고 가장 큰 값을 찾았다. nxt는 교환시마다 경우의 수들을 넣기 위한 임시공간이다.
# now에는 값들을 계속 갱신해준다.
# ===============================================================
# for tc in range(1, int(input()) + 1):
#
#     data, K = input().split()  # 숫자판의 정보, 교환횟수
#     K = int(K)    # 교환횟수
#     N = len(data) # 숫자판의 정보 의 길이
#
#     # 중복을 제거한 경우의 수를 담아주기 위한 set
#     now = set([data])
#     nxt = set()
#
#     print(now) # {'123'}
#
#     for _ in range(K):
#
#         while now: # now가 빌 때까지
#             s = now.pop() # pop()은 Set에서 원소를 하나씩 가져오는 함수입니다.
#             # print(f"--{s}--") # 123
#             s = list(s)
#             # print(f"--{s}--") # ['1', '2', '3']
#
#             for i in range(N):
#                 for j in range(i + 1, N):
#                     s[i], s[j] = s[j], s[i]
#                     # print(f"s--{s}--")
#                     # print(f"nxt--{nxt}--")
#
#                     nxt.add(''.join(s))
#                     # print(f"s--{s}--")
#                     # print(f"nxt--{nxt}--")
#
#                     s[i], s[j] = s[j], s[i]
#
#         print(f"now--{now}--")
#         print(f"nxt--{nxt}--")
#         now, nxt = nxt, now
#
#     print('#{} {}'.format(tc, max(map(int, now))))

# ===============================================================
# 완전탐색으로 풀려고 하면 시간초과가 생기기때문에 백트래킹, 가지치기 작업이 필요하다.
# ===============================================================
# 경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
def dfs(count):
    global answer

    # 횟수를 다 사용했다면
    if not count:
        # 숫자로 바꿔보고
        temp = int(''.join(values)) # ''.join(values) : 리스트에 있는 각 요소들을 하나의 문자열로 이어 붙이는 역할
        # 가지고 있는 최대수보다 크다면 갱신
        if answer < temp:
            answer = temp
        return

    # 바꿔야 하니까 이중 포문
    for i in range(length):
        # 경우의 수를 찾는거니까 i보다 큰위치부터
        for j in range(i + 1, length):
            # 두개의 위치를 바꾸고 나서
            values[i], values[j] = values[j], values[i]
            # 가지치기 해야하니까 일단 합쳐보고
            temp_key = ''.join(values)
            # 어떤수가 몇회차에 나왔는지 체크 => 1이면 안나온거니까 경우의수에 넣어주기
            if visited.get((temp_key, count - 1), 1): #숫자 0은 False로 간주되고, 0 이외의 숫자는 모두 True로 간주됩니다.
                # 이숫자는 몇회차에 사용했으니까 체크해주고
                visited[(temp_key, count - 1)] = 0
                # dfs도 돌려주고
                dfs(count - 1)
            # 다 썻으면 원상복귀
            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    # 바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    # 계속 쓸꺼니까 캐스팅
    length = len(values)
    # 가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t + 1, answer))