# 간단한 소인수분해
'''
숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.

[제약 사항]
N은 2 이상 10,000,000 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
'''
'''
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750
'''
# 실패코드
# n = int(input())
# up = [2,3,5,7,11]
#
# for _ in range(n):
#     a = int(input())
#
#     for i in range(5):
#         if i==0: print("#", end='')
#
#         b = a // up[i]
#
#         print(b, end=' ')
#
#         a -= up[i]**b

# =======================================================================
# 방법 1
# =======================================================================
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 입력으로 받은 N을
#     num = [2, 3, 5, 7, 11] # 소인수 리스트를 만들어서
#     count = [0, 0, 0, 0, 0] # 나눠진 횟수를 담기위한 빈 리스트 생성
#
#     # 리스트 num을 돌면서(range로 한 이유는 같은 인덱스에 count리스트에도 횟수를 추가해주기 위해서)
#     for n in range(len(num)):
#         # 무한루프를 주고
#         while True:
#             # 만약 N이 num의 n번째 숫자로 나눈 나머지가 0이라면
#             if N % num[n] == 0:
#                 # N은 그 숫자로 나눈 몫으로 바꾸고
#                 N = N//num[n]
#                 # count리스트의 같은 인덱스에 값을 +1해줌
#                 count[n] += 1
#             # 나눈 나머지가 0이 아니라면 멈추고 num의 다음 인덱스로 넘어감.
#             else:
#                 break
#     # 리스트컴프리핸션을 이용한 출력
#     # print('#{}'.format(tc),' '.join([str(_) for _ in count]))
#     # map함수는 str을 count의 모든항목에 적용
#     print('#{}'.format(tc), ' '.join(map(str, count)))
#     # print('#{}'.format(tc), (map(str, count))) #(x)
'''
'{}'.format(tc) : format 메소드는 중괄호({}) 위치에 format 함수 안의 인자를 문자열 형태로 삽입합니다. 
따라서, 이 부분은 tc의 값을 문자열로 변환하여 중괄호({}) 위치에 삽입합니다.
'''
'''
''.join(map(str, count)) : 여기서 map 함수는 count 리스트의 각 요소를 문자열로 변환하고, 
                            ' '.join() 함수는 이 문자열들을 공백(' ')으로 결합하여 하나의 문자열을 만듭니다. 
                            예를 들어, count가 [1, 2, 3]이라면 '1 2 3'이라는 문자열이 생성됩니다.
                            
* '구분자'.join(시퀀스) *
특정 구분자를 사용하여 주어진 시퀀스(리스트, 튜플, 딕셔너리, 문자열 등)의 항목들을 하나의 문자열로 결합하는데 사용
my_list = [1, 2, 3, 4, 5]
result = ' '.join(map(str, my_list))
print(result)  # 출력: "1 2 3 4 5"
'''
# =======================================================================
# 방법 2
# =======================================================================
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = [2,3,5,7,11]
    cnt_lst = [0,0,0,0,0]
    for i in range(5):
        while N % num_lst[i] == 0:
            cnt_lst[i] += 1
            N //= num_lst[i]
    print(f'#{tc} ', end='')
    print(*cnt_lst)
'''
리스트 언패킹(unpacking)
: 리스트의 요소들을 개별적인 값으로 분리하여 전달합니다.
def my_function(a, b, c):
    print(a)
    print(b)
    print(c)

my_list = [1, 2, 3]
my_function(*my_list)
# 출력:
# 1
# 2
# 3
'''