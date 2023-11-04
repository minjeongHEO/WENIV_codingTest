# 그리디 - 큰수의 법칙
#import sys
#input = sys.stdin.readline().rstrip()

# N : 배열의 크기
# M : 몇번 더하기
# K : 연속해서 더할 수 있는 수

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
# print(arr)

arr.sort()
# print(arr)

arr.reverse()
print(arr)

idx = 0
while M > 0:
    for _ in range(K):
        if M > 0:
            result += arr[0]
        else:
            break
        M -= 1

    if M > 0:
        result += arr[1]
        M -= 1

print(result)
''' 입력 예시
5 8 3 
2 4 5 4 6
'''
