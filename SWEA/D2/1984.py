# 중간 평균값 구하기

for tc in range(1,int(input())+1):
    arr = list(map(int, input().split()))
    arr.sort()
    s = set(arr)

    for idx, i in enumerate(s):
        if idx == 0 or idx == len(s)-1:
            arr.remove(i)

    avg = sum(arr)/len(arr)

    print(f"#{tc} {round(avg)}")
'''
58,768 kb
메모리
188 ms
실행시간
'''

# ======================================================
# 다른 방법
# ======================================================
T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
    print("#{} {}".format(test_case, round(sum(num_list)/len(num_list))))

'''
42,200 kb
메모리
96 ms
실행시간
'''