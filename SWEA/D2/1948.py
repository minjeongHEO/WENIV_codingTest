# 날짜 계산기
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, int(input())+1):
    result = 0
    a_month, a_day, b_month, b_day = map(int, input().split())

    if a_month == b_month:
        result = b_day - a_day + 1

    else:
        for i in range(a_month, b_month+1):
            if i == a_month:
                result += day[i] - a_day
            elif i == b_month:
                result += b_day
            else:
                result += day[i]

        result += 1

    print(f"#{tc} {result}")

