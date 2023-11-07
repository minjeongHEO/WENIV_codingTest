# 큰수부터 작은수
# n = int(input())
#
# # arr = []
# # for _ in range(n):
# #     arr.append(int(input()))
# arr = [int(input()) for _ in range(n)]
# arr.sort()  # 리스트를 오름차순으로 정렬
#
# for i in range(len(arr)-1, -1, -1):  # 인덱스를 역순으로 반복
#     print(arr[i], end=" ")

# =======================================================
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)  # 리스트를 내림차순으로 정렬

for num in arr:
    print(num, end=" ")

''' 입력코드
3
15
27
12
'''