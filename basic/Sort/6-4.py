array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# =========================================================
# 퀵 정렬 소스코드
# =========================================================
# def quick_sort(array, start, end):
#     if start >= end: # 원소가 1개인 경우 종료
#         return
#     pivot = start # 피벗은 첫 번째 원소
#     left = start + 1
#     right = end
#
#     while(left <= right):
#         # 1. 왼쪽에서 피벗보다 큰 데이터를 찾을 때까지 반복
#         while(left <= end and array[left] <= array[pivot]):
#             left += 1
#         # 2. 오른쪽에서 피벗보다 작은 데이터를 찾을 때까지 반복
#         while(right > start and array[right] >= array[pivot]):
#             right -= 1
#
#         # 3. 1번데이터와 2번데이터의 위치가 엇갈렸다면, 작은 데이터와 피벗을 교체
#         if(left > right):
#             array[right], array[pivot] = array[pivot], array[right]
#         else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 재수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
# quick_sort(array, 0, len(array) - 1)
#
# print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# =========================================================
# 파이썬의 장점을 살린 퀵 정렬 소스코드
# =========================================================
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    '''
    퀵 정렬 알고리즘에서는 피벗 값과 같은 값을 어느 쪽에 포함시킬지에 대한 정확한 규정은 없습니다. 
    따라서 피벗 값과 같은 값이 왼쪽 부분 리스트에 포함되든 오른쪽 부분 리스트에 포함되든 
    정렬 결과에는 영향을 주지 않습니다.
    '''
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    '''
    여기서는 피벗과 같은 값을 가진 다른 요소가 있을 경우 그 요소가 포함되는 것이지, 피벗이 중복해서 들어가는 것은 아닙니다.
    즉, [pivot]은 원래 배열에서 선택한 피벗을 의미하고, 
    left_side와 right_side는 피벗을 제외한 나머지 요소들 중에서 피벗과 비교하여 분류한 것입니다. 
    따라서 피벗 값이 중복으로 들어가는 것이 아닙니다.
    '''

print(quick_sort(array))