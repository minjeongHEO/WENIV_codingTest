# 가랏! RC카!
for tc in range(1, int(input())+1):
    n = int(input())
    result = 0
    speed = 0

    for i in range(n):
        # array = input().split()
        # #입력받은 문자열을 공백으로 분리하여 문자열의 리스트로 반환합니다.(문자열의 리스트를 반환)
        array = list(map(int, input().split()))
        # 입력받은 문자열을 공백으로 분리한 후, 각 문자열을 정수로 변환하여 정수의 리스트를 반환
        if array[0] == 1: #가속
           # speed += 1
           speed += array[1]
           # if speed > 2: speed = 2
           # print(f"가속 스피드:{speed}")

        elif array[0] == 2: #감속
            # speed -= 1
            if speed > array[1]:
                speed -= array[1]
            else:
                speed = 0

        result += speed

    print(f"#{tc} {result}")

