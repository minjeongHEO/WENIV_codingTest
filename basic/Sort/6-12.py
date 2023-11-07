# 두 배열의 원소 교체

n, k = map(int, input().split())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

arr_a.sort()
arr_b.sort(reverse=True)
# print(arr_a)
# print(arr_b)
for i in range(n):
    if k != 0:
        if arr_a[i] < arr_b[i]:
            arr_a[i], arr_b[i] = arr_b[i], arr_a[i]

        k -= 1

# print("----------------------")
print(sum(arr_a))


''' 입력코드
5 3
1 2 5 4 3
5 5 6 6 5
'''