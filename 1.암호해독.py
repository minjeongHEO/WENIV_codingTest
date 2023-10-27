#----------------------------- [  문제  ] --------------------------------
# 모든 알고리즘을 해독할 수 있는 알고리즘 7 원석를 보유한 알고리즘 제왕 파이와 썬은 죽기 전,
# 이 보물에 '암호'를 걸어 세계 어딘가에 묻어놨다고 공표하였다. 그가 남긴 문자는 아래와 같다.
# 섬으로 향하라!

# '   + -- + - + -   '
# '   + --- + - +   '
# '   + -- + - + -   '
# '   + - + - + - +     '

# 해(1)와 달(0),
# Code의 세상 안으로!(En-Coding)
#-------------------------------------------------------------------------
from typing import List

text=['   + -- + - + -   '
        ,'   + --- + - +   '
        ,'   + -- + - + -   '
        ,'   + - + - + - +     ']

print(text)

arr = []
# for i in text: # *1)
    # print(int(i.strip().replace(' ','').replace('+','1').replace('-','0')))

    # ---------,2를 붙이면 문자열을 이진법으로 인식해서 십진수(숫자)로 바꿔준다.
    # * 문자열('1001010') ➡ 2진법숫자로 변경(74) ➡ 문자로 변경('J')
    # * string           ➡ int(string,2)     ➡ chr(int(string,2))

    # print(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2))

    # ---------Built-in-function
    # 1. ord() : 문자 ➡ 숫자로 변경
    # 2. chr() : 숫자 ➡ 문자로 변경
    # 3. zfill() : # *2)
    # chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2))
    # arr.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))
    # print(arr) #['J', 'E', 'J', 'U']
    # print(''.join(arr)) #JEJU

## ---------위 코드를 한 줄로 만들어보자.
# 1. text를 순회하기
# 2. i for i in text: 의 앞에 i값에 위의 코드를 넣으면 한 줄로 작성이 가능하다.

# print([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text]) #'J', 'E', 'J', 'U']
# print(''.join([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text])) #JEJU


# *1) 파이썬에서 'for' 루프를 사용하려면 반드시 루프 내부에 실행할 코드가 있어야 합니다.
#   그렇지 않으면 SyntaxError가 발생합니다. 예를 들어, 다음과 같은 코드는 에러를 발생시킵니다
#   for i in range(10):
#   위 코드는 'for' 루프를 시작했지만 루프 내부에 실행할 코드가 없으므로 에러가 발생합니다.



# ---------리스트 컴프리헨션 사용해보기
# for i in range(10): i
#
# 🔽 (리스트 컴프리헨션)
# [i for i in range(10)]
#
# 🔽 (짝수만 골라내기)
# [i for i in range(10) if i%2 == 0]
#
# 🔽 (구구단 짜보기)
# gugu = [f'{i}*{j}={i*j}' for i in range(2,10) for j in range(1,10)]
# print(gugu)

# *2) zfill(n)
# : n자리 숫자로 맞춰준다.
# print('111'.zfill(10))

# ---------함수형으로 사용해보기
sample1 = [int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2) for i in text]
sample2 = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]
print(sample1)
print(sample2)

# -----1. lamda 사용
print('-----1. lambda 함수 사용')
print(list(map(lambda x :  chr(int(x,2)), sample2)));
print(''.join(list(map(lambda x :  chr(int(x,2)), sample2))));

# -----2. map 함수 사용
print('-----2. map 함수 사용')
# map(function, sample2)
def func(x):
    return chr(int(x,2))
print(list(map(func,sample2))) #list를 안붙이면 주소값만 나옴 <map object at 0x0000026BC61FB970>
print(''.join(list(map(func,sample2))))

# -----3. zip 함수 사용
# zip 함수는 주로 여러 개의 반복 가능한 객체를 동시에 순회하며, 각 객체에서 같은 위치에 있는 요소들을 묶어 처리할 때 사용됩니다.
# 주어진 상황에서는 단일 리스트의 요소들을 독립적으로 처리하는 것이므로,
# zip 함수의 사용이 적합하지 않지만, 아래와 같이 각각의 문자열을 개별 리스트로 취급하고,
# 동일 위치의 문자들을 묶어서 처리하는 방식으로 zip 함수를 사용할 수 있습니다.

