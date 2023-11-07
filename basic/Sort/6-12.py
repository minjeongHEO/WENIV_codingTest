# 두 배열의 원소 교체

n, k = map(int, input().split())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

arr_a.sort()
arr_b.sort(reverse=True)
# print(arr_a)
# print(arr_b)

# 첫 번째 로직은 N번의 반복문을 돌면서, K번의 교환이 완료되었는지를 매번 확인합니다.
# 이 경우 최악의 시나리오에서는 N번의 반복문이 모두 실행되어야 하므로, 시간 복잡도는 O(N)입니다.
# for i in range(n):
#     if k != 0:
#         if arr_a[i] < arr_b[i]:
#             arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
#
#         k -= 1

# 두 번째 로직은 최대 K번의 반복문만을 돌며, A의 원소가 B의 원소보다 크거나 같을 때 반복문을 즉시 중단합니다.
# 이 경우 최악의 시나리오에서도 K번의 반복문이 모두 실행되므로, 시간 복잡도는 O(K)입니다.
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if arr_a[i] < arr_b[i]:
        # 두 원소를 교체
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

# 따라서, K가 N에 비해 상대적으로 작은 경우에는 두 번째 로직이 더 효율적입니다.


# print("----------------------")
print(sum(arr_a))

''' 입력코드
5 3
1 2 5 4 3
5 5 6 6 5
'''