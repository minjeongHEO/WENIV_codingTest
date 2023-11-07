# 성적이 낮은 순서로 학생 출력하기
# 학생의 정보가 최대 100,000개 까지 입력될 수 있으므로
# 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나
# O(N)을 보장하는 계수 정렬을 이욯한다.
#
# 파이썬의 튜플 문법

n = int(input())

arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

print(arr) # [('홍길동', 95), ('이순신', 77)]

# !!!! key를 이용하여 점수를 기준으로 정렬
arr = sorted(arr, key=lambda student: student[1])
'''
 sorted() 함수의 두 번째 인자는 정렬 기준을 정하는 함수를 지정하는 곳입니다.
'''

# 정렬이 수행된 결과를 출력
for i in arr:
    print(i[0], end=" ")

''' 입력코드
2
홍길동 95
이순신 77
'''