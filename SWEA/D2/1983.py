# 조교의 성적 매기기
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

# 총점 = 중간고사 35% + 기말고사 45% + 과제 20%
t = int(input())


for tc in range(1, t+1):
    # 학생수 N 과, 학점을 알고싶은 학생의 번호 K
    n, k = map(int, input().split())
    # seq = []
    dic = {}
    for i in range(n):
        a, b, c = map(int, input().split())
        # final = round(a*0.35 + b*0.45 + c*0.2, 0)
        final = a*0.35 + b*0.45 + c*0.2
        # seq.append({i:final})

        # 애초에 하나의 딕셔너리로 만들거나
        dic[i] = final

        # if i == k-1:
        #     print(f"i:{i}, final:{final}")

        # print(seq)
        #[{0: 74.0}, {1: 97.0}, {2: 90.0}, {3: 99.0}, {4: 72.0}, {5: 82.0}, {6: 97.0}, {7: 72.0}, {8: 92.0}, {9: 85.0}]
        # print(dic)
        #{0: 74.0, 1: 97.0, 2: 90.0, 3: 99.0, 4: 72.0, 5: 82.0, 6: 97.0, 7: 72.0, 8: 92.0, 9: 85.0}

    # 배열을 하나의 딕셔너리로 합치기
    # merged = {list(d.keys())[0]: list(d.values())[0] for d in seq}

    # value값 기준으로 내림차순 정렬
    sorted_data = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_data)
    # [(3, 99.0), (1, 97.0), (6, 97.0), (8, 92.0), (2, 90.0), (9, 85.0), (5, 82.0), (0, 74.0), (4, 72.0), (7, 72.0)]
    # [(3, 99.45), (6, 96.25), (1, 92.55000000000001), (2, 88.8), (5, 85.85000000000001), (9, 85.75), (8, 85.5), (0, 74.6), (4, 72.35), (7, 68.95)]

    # key값이 k인 값과 몇번쨰 인덱스인지 찾기
    # sorted_data.index(key=k) #index함수는 리스트에서 사용하는 함수로 딕셔너리에서 사용불가
    index = -1
    for i, (key, _) in enumerate(sorted_data):
        if key == k - 1:  # 학생 번호는 1부터 시작하므로 1을 빼줍니다.
            index = i
            break
    '''
    enumerate(sorted_data)가 생성하는 각 항목은 두 부분으로 구성됩니다. 첫 번째 부분은 항목의 인덱스이고, 두 번째 부분은 원래 리스트의 항목입니다.
    여기서 원래 리스트 sorted_data의 각 항목은 (key, value) 형태의 튜플이므로, 두 번째 부분을 튜플로 분해하여 key와 _에 각각 할당하고 있습니다.
    _는 관습적으로 "이 변수의 값은 사용되지 않는다"는 것을 나타내는 데 사용하는 변수 이름입니다. 이 경우, 각 튜플의 value는 필요하지 않으므로 _로 표시하여 그 값을 무시하고 있습니다.
    따라서 for i, (key, _) in enumerate(sorted_data): 구문은 "인덱스와 key를 각각 i와 key에 할당하고, value는 무시하라"는 의미입니다.
    '''

    grade_index = index // (n // 10)
    '''
    N/10명의 학생들에게 동일한 평점을 부여할 수 있다는 건
    만약 30명의 학생이 있으면, 3명씩 평점이 같겠네!
    '''

    print("#{} {}".format(tc, grade[grade_index]))

'''
58,768 kb
메모리
160 ms
실행시간
'''

# =====================================================================
# 다른 풀이
# =====================================================================
# score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
#
# t = int(input())
# for tc in range(1, t + 1) :
#     n, k = map(int, input().split())
#     data = []
#     for _ in range(n) :
#         a, b, c = map(int, input().split())
#         sum_value = (a * 0.35) + (b * 0.45) + (c * 0.2)
#         data.append(sum_value)
#
#     k_score = data[k-1]
#     data.sort(reverse=True)
#
#     value = n // 10
#     result = data.index(k_score) // value
#
#     print("#%d %s" % (tc, score[result]))
'''
58,784 kb
메모리
167 ms
실행시간
'''

'''
1
10 2
87 59 88
99 94 78
94 86 86
99 100 99
69 76 70
76 89 96
98 95 96
74 69 60
98 84 67
85 84 91
'''
