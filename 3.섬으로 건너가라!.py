#----------------------------- [  문제  ] --------------------------------
# 1. 한 배에는  탈 수 있는 인원이 정시에는 25명, 10분마다 15명씩 탈 수 있습니다.
# 2. 배는 매일 9시부터 21시 전까지(21시를 포함하지 않습니다) 10분단위로 들어옵니다.
# 3. 전체 대기 인원은 14,000,605명입니다. 우리는 14,000,606번째와 14,000,607번째에 배를 타게 됩니다. 14119200
#       앞사람이 아프거나, 대기를 못하고 빠질 경우 대기인원이 줄어들 수도 있습니다.
#       **라이캣과 자바독이 다른 배를 타야 할 경우에는 뒷배를 타야 합니다.**
# 4.  10월까지밖에 없습니다.
# 5. 시간의 개념은 동일합니다. (하루는 24시간, 1시간 60분, 1분 60초)
#     - **현재 날짜는 2020년 1월 1일 입니다.**
# 6. 배에 타는 순간 자바독이 화장실이 급하다 하여 화장실에 갔으며, 현재시간에 '분'만큼 배 출발이 늦어졌습니다.
# 7. 배는 휴일도 동일하게 운항됩니다. 배는 천재지변에 영향을 받지 않습니다. 마법으로 날아다니거든요.
#
# 8. **라이캣과 자바독이 배에 타는 날짜를 구하세요.**

# 입력
# 대기인원 = 14000605
#
# 출력
# 2025년 2월 413일 11시 0분 출발
#
# 입력
# 대기인원 = 1200202
#
# 출력
# 2020년 1월 1000일 11시 0분 출발

#-------------------------------------------------------------------------

# 앞사람이 아프거나, 대기를 못하고 빠질 경우 대기인원이 줄어들 수도 있습니다.
# => 얘를 어떻게 풀어야 할지 모르겠네

# 1. 배는 매일 09시 ~ 20시59분
# 2. 매 시간당 배는 6번운항, 100명 수용
# 3. 하루에 총 배는 72번(6번x12), 1200명(100명x12) 수용
# 4. 일자는 모두 2의 n승


def solution_func(num):
    waiting_num = 0
    year = 2020
    month = 0
    # while waiting_num >= 14000606 and waiting_num >= 14000607:
    #     year += 1
    #     for i in range(10, 0, -1):
    #         waiting_num += (2**i) * 1200 # JS : waiting_num += Math.pow(2, i) * 1200
    #         print(f"{i}월은 {2**i}일")
    #         print(f" +{(2**i) * 1200} 명 수용")
    #         print(waiting_num)
    #
    #         if waiting_num >= 14000606 and waiting_num >= 14000607:
    #             month = i
    #         #     print(f"{month}월 {waiting_num % (2 ** month)}일")
    #             break

    check = False
    while True:

        for i in range(10, 0, -1):
            waiting_num += (2 ** i) * 1200

            if i == 10: month = 1
            elif i == 9: month = 2
            elif i == 8: month = 3
            elif i == 7: month = 4
            elif i == 6: month = 5
            elif i == 5: month = 6
            elif i == 4: month = 7
            elif i == 3: month = 8
            elif i == 2: month = 9
            elif i == 1: month = 10

            print(f"{month}월은 {2 ** i}일")
            print(f" +{(2 ** i) * 1200} 명 수용")
            print(waiting_num)

            if waiting_num >= (num+1) and waiting_num >= (num+2):
                check = True
                break
        if check:
            break

        # for j in range(1, month):
        #     waiting_num -=

        year += 1

    return print(f"{year}년 {month}월")
    # return print(f"{year}년 {month}월 {i for in range(1,month+1)}일)
    # print(f"{year}년 {month}월 {waiting_num%(2**month)}일")

solution_func(14000605)

