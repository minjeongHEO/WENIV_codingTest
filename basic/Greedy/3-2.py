# 그리디 - 큰수의 법칙
#import sys
#input = sys.stdin.readline().rstrip()

# N : 배열의 크기
# M : 몇번 더하기
# K : 연속해서 더할 수 있는 수

# ------------- 1. arr.reverse() 사용안하고 구하기 -------------
# N, M, K = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# first = arr[N-1]    #가장 큰 수
# second = arr[N-2]   #두번째로 큰 수
#
# result = 0
#
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += first
#         M -= 1
#
#     if M == 0:
#         break
#     result += second
#     M -= 1
#
# print(result)

# ------------- 2. 더 효율적으로 구하기 -------------
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() # 입력 받은 수들 정렬하기
first = arr[N - 1] # 가장 큰 수
second = arr[N - 2] # 두 번째로 큰 수

# ** 가장 큰 수가 더해지는 횟수 계산 **
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (M - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력

'''
** 가장 큰 수가 더해지는 횟수 계산 **
- (k + 1)은 한 세트로 봤을 때, 
가장 큰 수가 연속으로 등장할 수 있는 횟수(k)와 두 번째로 큰 수가 등장하는 횟수(1회)를 합친 것
가장 큰 수가 k번, 두 번째로 큰 수가 1번 등장하는 패턴이 (k + 1)입니다.

- 전체 연산 횟수 m을 (k + 1)로 나누면 이 패턴이 몇 번 반복될 수 있는지를 알 수 있습니다. 

- 그리고 이때 가장 큰 수가 등장하는 횟수는 
패턴이 반복되는 횟수에 k를 곱한 것이므로 int(m / (k + 1)) * k가 됩니다.

- 전체 연산 횟수 m이 (k + 1)로 딱 떨어지지 않을 경우를 고려해야 합니다. 
따라서 m % (k + 1)를 이용해서 나머지 연산 횟수가 있을 경우, 그 횟수만큼 가장 큰 수를 추가로 더해줍니다.

- ex)_
예를 들어, m이 7이고, k가 3이라고 하면, 
m / (k + 1)은 1이고, m % (k + 1)은 3이므로 
가장 큰 수가 더해지는 횟수는 1 * 3 + 3 = 6회가 됩니다. 
즉, 가장 큰 수를 6번, 두 번째로 큰 수를 1번 더하는 것이 최대의 합을 만들어냅니다.
'''

# ============================================================
# N, M, K = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0
# # print(arr)
#
# arr.sort()
# # print(arr)
#
# arr.reverse()
# print(arr)
#
# idx = 0
# while M > 0:
#     for _ in range(K):
#         if M > 0:
#             result += arr[0]
#         else:
#             break
#         M -= 1
#
#     if M > 0:
#         result += arr[1]
#         M -= 1
#
# print(result)


''' 입력 예시
5 8 3 
2 4 5 4 6
'''
