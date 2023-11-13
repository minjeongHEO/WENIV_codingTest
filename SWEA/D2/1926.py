# 간단한 369게임
# "3" "6" "9"
# 박수는 "-"

result = ""
n = int(input())
for i in range(1, n+1):

    arr = list(str(i))

    if "3" in arr or "6" in arr or "9" in arr:
        result += "-" * arr.count("3")
        result += "-" * arr.count("6")
        result += "-" * arr.count("9")
        result += " "
    else:
        result += str(i)
        result += " "

print(result)
'''
58,552 kb
메모리
140 ms
실행시간
'''

# ===================================================
# 다른 풀이
# ===================================================
n = int(input())

arr = []

for i in range(1, n+1):
    ns = str(i)

    clap = ns.count('3') + ns.count("6") + ns.count("9")

    if clap == 0:
        print(i, end=" ")
    else:
        print("-" * clap, end=' ')

'''
42,212 kb
메모리
93 ms
실행시간
'''