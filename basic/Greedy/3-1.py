# coin_types = [500, 100, 50, 10]
# result = []
# n = 1260
#
# for i in range(len(coin_types)):
#     count = n // coin_types[i]
#
#     n = n % coin_types[i]
#
#     result.append({f"{coin_types[i]} 원 ":f"{count}개" })
#
# print(result)

# --------------------------------------
# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
n = 1260
count = 0

for i in coin_types:
    count += n // i # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n = n % i

print(count)

