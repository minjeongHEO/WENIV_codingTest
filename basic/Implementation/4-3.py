# 왕실의 나이트 - 구현
# 수평으로 두간 이동 후 수직으로 한칸
# 수직으로 두칸 이동 후 수평으로 한칸
#
# 좌표는  8x8
#
# 행 위치는 숫자 1~8
# 열 위치는 영어 a~h

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
'''
input_data의 첫 번째 문자(열 위치)를 숫자로 변환하는 과정입니다. 
ord() 함수는 문자의 ASCII(아스키) 코드 값을 반환합니다. 
    (
    print(ord('A'))  # 출력: 65
    print(ord('a'))  # 출력: 97
    print(ord('1'))  # 출력: 49
    반대로 아스키 코드 값을 문자로 변환하고 싶을 때는 chr() 함수를 사용합니다. 
    예를 들어, chr(65)는 'A'를 반환합니다.
    )
'a'의 아스키 코드 값은 97이므로, 'a'를 기준으로 열의 위치를 숫자로 변환합니다. 

예를 들어, 'a'에서 'a'를 추출하면 아스키 코드 값이 동일하므로 0이 되고, 
    여기에 1을 더하여 column에 1을 할당합니다.
'''

# 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2) ]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # print(type(step)) <class 'tuple'>
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

