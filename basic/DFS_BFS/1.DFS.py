def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9 # [False, False, False, False, False, False, False, False, False]

# 정의된 DFS함수 호출
dfs(graph, 1, visited)

print("")

# *************************************************************
# stack / 스택에 마지막으로 입력된 자료가 제일 먼저 삭제 하는 방식 LIFO(Last In First Out)
# *************************************************************
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print("-------stack--------")
print(stack[::-1])  #스택의 최상단 원소부터 출력 //[1, 3, 2, 5]
print(stack)        #스택의 최하단 원소부터 출력 //[5, 2, 3, 1]

# *************************************************************
# queue / 왼쪽에서 들어와서 오른쪽에서 나간다 FIFO(First In First OUT)
# *************************************************************
# 덱 객체 생성 후 사용
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print("-------queue--------")
print(queue)    # 먼저 들어온 순서대로 출력 //deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력 //deque([4, 1, 7, 3])

# *************************************************************
# 재귀 함수 / Recursive Function ; 자기 자신을 다시 호출하는 함수
# *************************************************************
# 1) 팩토리얼
# 수학적으로 0! 과 1! 의 값은 1이다.
#
# 2) 유클리드 호제법 (최대공약수 계산)
# - 유클리드 호제법
#   두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 하자(A%B)
#   이 때 A,B의 최대공약수는 B와 R의 최대공약수와 같다.


# A = GCD * α
# B = GCD * β
#
# 그러면 A의 배수이면서 동시에 B의 배수인 것 중 가장 최소인 최소공배수(LCM)는
#
# LCM   =  GCD * α * β
# 즉,      =  A* β  = B * α
# 따라서 = (A*B) / GCD  이다.

