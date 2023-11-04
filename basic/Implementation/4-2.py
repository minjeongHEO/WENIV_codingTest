# 시각 - 구현
# 정수 n => 00시:00분:00초 ~  N시:59분:59초 중에서 3이 포함되는 모든 경우의 수

h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            
            if '3' in str(i)+str(j)+str(k): # 여기서 문자열 더해서 조건절에 넣을 수 있음
                count += 1

print(count)