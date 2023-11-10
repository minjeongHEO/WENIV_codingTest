for tc in range(1,int(input())+1):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    print(f"#{tc} {' '.join(map(str,array))}")

# ============================================
# 방법 2
# for test in range(1,int(input())+1):
#     n = int(input())
#     array = list(map(int, input().split()))
#     a = sorted(array)
#     print(f"#{test}", *a)