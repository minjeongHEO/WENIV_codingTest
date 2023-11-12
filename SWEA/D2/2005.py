# 파스칼의 삼각형
'''
58,532 kb
메모리
143 ms
실행시간
'''
for tc in range(1,int(input())+1):
    n = int(input())
    arr = [[0]*(n+1) for _ in range(n+1)]
    print(arr)

    for i in range(1,n+1): #1~4 1

        for j in range(i): #0 1 2 3 j= 0
            if j == 0 or j == i-1:
                val = 1
            else:
                val = arr[i-1][j-1] + arr[i-1][j]

            arr[i][j] = val


    print(f"#{tc}")
    for index,i in enumerate(arr):
        if index == 0:
            continue
        else:
            print(*i[:index])


# =====================================================
# 처음에 모든 값을 0으로 초기화하는 2차원 리스트를 만드는 대신,
# 필요한 만큼만 리스트를 확장하는 방식을 사용하면 메모리를 더 효율적으로 사용할 수 있습니다.
# =>
# =====================================================
'''
58,764 kb
메모리
171 ms
실행시간
'''
print("++++++++++++++++++++++++++++++")
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[0]*i for i in range(1, n+1)]
    print(arr)
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                val = 1
            else:
                val = arr[i-1][j-1] + arr[i-1][j]

            arr[i][j] = val

    print(f"#{tc}")
    for row in arr:
        print(*row)
'''
리스트를 필요한 만큼만 생성하는 방식으로, 이론적으로는 메모리 사용이 더 효율적일 것이라고 예상했습니다. 그러나 실제로는 파이썬의 리스트 동작 방식과 관련된 몇 가지 요소로 인해 반대의 결과가 나왔을 수 있습니다.

리스트 크기 변경: 파이썬 리스트는 동적 배열로 구현되어 있어, 리스트의 크기를 변경할 때 추가적인 메모리를 요구합니다. 리스트를 늘리는 작업은 내부적으로 새로운 메모리 공간을 할당하고 기존의 데이터를 복사하는 과정을 포함하므로, 이 과정에서 추가적인 시간이 소요될 수 있습니다.
리스트 생성 비용: 리스트를 생성하는 데에도 일정한 비용이 들며, 이 비용은 리스트의 크기에 비례합니다. 따라서 작은 크기의 리스트를 여러 번 생성하는 것이 큰 크기의 리스트를 한 번 생성하는 것보다 비용이 더 클 수 있습니다.
캐시 효율성: 컴퓨터의 메모리 접근 패턴에 따라 캐시 효율성이 달라집니다. 연속적인 메모리 공간에 접근하는 것이 불연속적인 공간에 접근하는 것보다 빠를 수 있습니다. 초기 코드에서는 2차원 리스트가 연속적인 메모리 공간에 할당되지만, 제안한 코드에서는 리스트마다 별도의 메모리 공간에 할당됩니다. 이 차이로 인해 실행 시간에 차이가 발생했을 수 있습니다.
결론적으로, 두 코드 사이의 성능 차이는 파이썬의 내부 동작 방식과 관련이 있으며, 이는 종종 직관적이지 않은 결과를 초래할 수 있습니다. 그러므로, 어떤 방식이 더 효율적인지를 판단할 때는 다양한 요소를 고려해야 합니다.
'''