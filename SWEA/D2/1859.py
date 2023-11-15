# 백만 장자 프로젝트

for tc in range(1, int(input())+1): # TC마다
    N = int(input()) #배열의 길이 (안쓰임)
    arr = list(map(int, input().split())) #배열 입력 받기

    answer = 0 #출력할 정답
    sellPrice = 0 #현재 판매가격(최댓값)

    for val in arr[::-1]: # 배열 거꾸로 순회
        if val >= sellPrice: #현재 값이 최댓값보다 크거나 같다면
            sellPrice = val #최댓값 업데이트
        else:
            answer += sellPrice - val #아니라면 정답값에 가격차이를 더한다. (현재 값에 구매해서 최댓값에 판다)
    print(f"#{tc} {answer}") #출력 양식에 맞춰서 출력
'''
243,316 kb
메모리
1,245 ms
실행시간
'''
    # print('#', tc, " ", answer, sep="") #이거뭐지? sep

# -------------------------------------------------------------
# 다른 풀이 1
# -------------------------------------------------------------
# 테스트 케이스 개수 T 입력
T = int(input())

# T만큼 반복
for tc in range(1, T + 1):
    # 자연수 N의 개수 입력
    N = int(input())
    # N 리스트 입력
    N_list = list(map(int, input().split()))

    # N_list의 마지막 값을 최대값으로 설정
    max_value = N_list[-1]
    # 이익 변수 초기화
    profit = 0

    # N-2번째 인덱스부터 0번째 인덱스까지 1씩 감소하면서 반복 순회
    for i in range(N - 2, -1, -1):
        # 만약 현재 매매가가 최대값보다 크면 최대값을 변경
        if N_list[i] >= max_value:
            max_value = N_list[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 profit 변수에 더해준다
        else:
            profit += max_value - N_list[i]

    # 결과 출력
    print('#{} {}'.format(tc, profit))
'''
250,748 kb
메모리
1,161 ms
실행시간
'''

# -------------------------------------------------------------
# 다른 풀이 2
# -------------------------------------------------------------
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    a = list(map(int, input().split()))

    sell = 0
    maxnum = a.pop()

    for i in reversed(a):
        if i > maxnum:
            maxnum = i
        else:
            sell += maxnum - i

    print('#{} {}'.format(test_case, sell))

'''
237,144 kb
메모리
1,117 ms
실행시간
'''