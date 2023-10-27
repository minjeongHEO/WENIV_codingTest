#----------------------------- [  문제  ] --------------------------------
# * 친구들은 추가 될 수도, 덜 건널 수도 있음
# 루비독, 피치피독, 씨-독, 코볼독
#
# 1. 각 돌들이 얼마나 버틸수 있는지 배열로 주어집니다.
#     (내구도 0까지는 독의 몸무게를 버틸 수 있습니다. 0미만이 되면 독은 살아남지 못합니다.)
#
# 2. 각 독들의 개인정보가 JSON으로 주어집니다.
#     개인정보는 보호되지 않습니다.
#     (JSON은 큰 따옴표로 묶여야 합니다. 가능하다면 json을 import하여 풀어보세요!)
#
# 3. 각 돌에 독들이 착지할 때 돌의 내구도는 몸무게만큼 줄어듭니다.
#     ex) [1,2,1,4] 각 돌마다 몸무게 1인 독 1마리 2마리 1마리 4마리의 착지를 버틸 수 있습니다.
#
# 4. 독들의 점프력이 각자 다릅니다.
#     ex) 점프력이 2라면 2칸씩 점프하여 착지합니다.
#-------------------------------------------------------------------------

# 파이썬의 변수명은 일반적으로 snake_case 형식을 따릅니다
# JavaScript에서는 변수명을 지을 때 주로 camelCase 형식을 사용합니다.

# 첫번째 케이스
dog_json = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

rock_power = [1, 2, 1, 4] # 돌의 내구도

# 두번째 케이스
# dog_json = [{
#     "이름" : "루비독",
#     "나이" : "95년생",
#     "점프력" : "3",
#     "몸무게" : "4",
#     },{
#     "이름" : "피치독",
#     "나이" : "95년생",
#     "점프력" : "3",
#     "몸무게" : "3",
#     },{
#     "이름" : "씨-독",
#     "나이" : "72년생",
#     "점프력" : "2",
#     "몸무게" : "1",
#     },{
#     "이름" : "코볼독",
#     "나이" : "59년생",
#     "점프력" : "1",
#     "몸무게" : "1",
#     },
# ]
# rock_power = [5, 3, 4, 1, 3, 8, 3]

# print(dog_json.length) # js
print(len(dog_json))    # py

SAVE_DOG = []
for i in dog_json:
    dog_weight = int(i["몸무게"])
    dog_name = i["이름"]
    dog_jump = int(i["점프력"])

    weight_check = False

    for j in rock_power:
        if(j < dog_weight):
            weight_check = True
            break

    if(weight_check):
        continue

    # print(`---${dogName}`)        # js
    print(f"----'{dog_name}' 의----")   # py
    print(f"---점프력:{dog_jump}")  # py
    print(f"---몸무게:{dog_weight}")  # py

    print(f"이전{rock_power}")
    #점프력으로 계속 len(rockPower)이 넘을 때까지
    dog_location = dog_jump - 1
    while dog_location < len(rock_power):
        rock_power[dog_location] -= dog_weight
        dog_location += dog_jump

        if dog_location > len(rock_power):
            SAVE_DOG.append(dog_name)
            break  # 반복문을 빠져나옵니다.

    print(f"이후{rock_power}")


print(f"SAVE_DOG : {SAVE_DOG}")






