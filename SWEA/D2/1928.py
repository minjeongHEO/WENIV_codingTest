# Base64 Decoder
# ===============================================================================
# 방법1. 라이브러리 (X)
# ===============================================================================
# T = int(input())
# 표 1
# decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
#           'W', 'X', 'Y', 'Z',
#           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#           'w', 'x', 'y', 'z',
#           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
#           ]
#
# for tc in range(1, 1 + T):
#
#     # 입력받는 글자(인코딩 된 상태)
#     word = list(input())
#
#     # 글자의 길이
#     length = len(word)
#
#     # word의 글자 -> 표1에 따라 숫자로 변환 -> 이진수로 변환 -> 하나의 res로 만들기
#     res = ''
#
#     for q in range(length):
#
#         # word -> 표1에 따라 숫자로 변환
#         num = decode.index(word[q])
#
#         # num -> 이진수로 변환
#         # int형태로 더하면 단순 숫자의 합이 나오므로 str로 변환하고 앞의 0b 제거
#         bin_num = str(bin(num)[2:])
#
#         # bin_num의 길이가 6보다 작으면 앞에 0 붙여주기
#         # 1을 이진수로 바꾸면 1로 나옴(필요한 값은 000001임)
#         while len(bin_num) < 6:
#             bin_num = '0' + bin_num
#
#         res += bin_num
#
#     # 문제에서 구하고자 하는 원래 문장
#     r = ''
#
#     # 글자의 길이 * 6에서 8비트씩 자름
#     for w in range(length * 6 // 8):
#         # 8비트씩 자르기
#         # 자른 값을 10진수로 변환
#         e = int(res[w * 8:w * 8 + 8], 2)
#
#         # 아스키코드의 값을 r에 추가
#         r += chr(e)
#
#     print('#{} {}'.format(tc, r))

# ===============================================================================
# 방법 2. 라이브러리 (O)
# ===============================================================================
from base64 import b64decode

T = int(input())
str = '안녕?'
bytes = str.encode('UTF-8')

print(str)
print(bytes)
print("")

for tc in range(1, T + 1):
    word = input()
    print(word)
    res = b64decode(word).decode('UTF-8')
    print(res)
    print('#{} {}'.format(tc, res))

# base64는 바이너리 데이터를 ASCII 문자만으로 표현하기 위해 만들어진 인코딩 방법이다.
# ASCII 문자 하나가 64진법 숫자 하나를 의미하기 때문에 BASE64라는 이름을 가지게 되었다.
# 파이썬에서는 base64 모듈을 통해서 바이너리 데이터를 base64로 인코딩하거나
# base64로 표현된 정보를 디코딩해서 바이너리 데이터로 가져올 수 있다.









