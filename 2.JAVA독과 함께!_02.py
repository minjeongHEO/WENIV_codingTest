# import json
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

# *****************첫번째 케이스*****************
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
# rock_power = [1, 2, 1, 4] # 돌의 내구도
# 생존자 : ['씨-독']

# *****************두번째 케이스*****************
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
rock_power = [5, 3, 4, 1, 3, 8, 3]
# 생존자 : ['루비독', '씨-독']

# print(dog_json.length) # js
# print(len(dog_json))    # py

SAVE_DOG = []

# 1
# def solution_func(rock_power, dogs):
#     answer = [dogs[i]["이름"] for i in range(len(dogs))]
#     return answer
#
# print(solution_func(rock_power, dog_json))

# 2
# def solution_func(rock_power, dogs):
#     answer = [i["이름"] for i in dogs]
#     return answer
#
# print(solution_func(rock_power, dog_json))

# 3
# def solution_func(rock_power, dogs):
#     answer = [i["이름"] for i in dogs]
#
#     for i in dog_json:
#         dog_location = 0
#         while dog_location <  len(rock_power)-1:
#             dog_location += int(i["점프력"])
#             rock_power[dog_location-1] -= int(i["몸무게"])
#             if rock_power[dog_location-1] < 0:
#                 answer[answer.index(i["이름"])] = "fail"
#                 break
#
#     return [i for i in answer if i!= "fail"]
#
# print(solution_func(rock_power, dog_json))

# 4
def solution_func(rock_power, dogs):
    answer = [i["이름"] for i in dogs]
    for i in dog_json:
        dog_location = 0
        while dog_location <  len(rock_power)-1:
            dog_location += int(i["점프력"])
            rock_power[dog_location-1] -= int(i["몸무게"])
            if rock_power[dog_location-1] < 0:
                del answer[answer.index(i["이름"])] # *2) *3)
                # answer.remove(i["이름"]) # del 대신 remove 사용
                break
    return answer

print(solution_func(rock_power, dog_json))

# print(type(dog_json)) #list
# 상단에 import 필요! import json
# print("********* json.dumps *********")
# JSON독  = json.dumps(dog_json, ensure_ascii=False) #ensure_ascii=False : 한글(비아스키 문자) 그대로 유지
# print(JSON독)
# print(JSON독[0]) # [
# print(JSON독[:10]) # [{"이름": "루
# print(type(JSON독))   #string

# print("********* json.loads ***********")
# JSON독  = json.loads(JSON독)
# print(JSON독)
# print(JSON독[0]) # {'이름': '루비독', '나이': '95년생', '점프력': '3', '몸무게': '4'}
# print(JSON독[:10]) # [{'이름': '루비독', '나이': '95년생', '점프력': '3', '몸무게': '4'}, {'이름': '피치독', '나이': '95년생', '점프력': '3', '몸무게': '3'}, {'이름': '씨-독', '나이': '72년생', '점프력': '2', '몸무게': '1'}, {'이름': '코볼독', '나이': '59년생', '점프력': '1', '몸무게': '1'}]
# print(type(JSON독))   #list

# /////////////// 나의 풀이 /////////////////
# for i in dog_json:
# # for index, i in enumerate(dog_json): # *1)
#     dog_weight = int(i["몸무게"])
#     dog_name = i["이름"]
#     dog_jump = int(i["점프력"])
#
#     weight_check = False
#
#     dog_location = dog_jump - 1
#     while dog_location < len(rock_power):
#         if rock_power[dog_location] < dog_weight:
#             rock_power[dog_location] = 0
#             weight_check = True
#             break
#
#         rock_power[dog_location] -= dog_weight
#         dog_location += dog_jump
#
#         if dog_location+1 > len(rock_power):
#             SAVE_DOG.append(dog_name)
#             break  # 반복문을 빠져나옵니다.
#
#     if weight_check:
#         continue
#
#
# print(f"SAVE_DOG : {SAVE_DOG}")
# /////////////////////////////////////////

#
# *1)
# 파이썬에서는 enumerate() 함수를 사용하여 반복문을 돌면서 인덱스 값을 함께 얻을 수 있습니다.
# 이 함수는 반복 가능한 객체(리스트, 튜플, 문자열 등)를 입력 받아 인덱스 값과 함께 원소를 반환합니다.
#
# *2)
# remove : 리스트.remove(값)
#           O(N)
# del : del 리스트[인덱스]
#       일반적으로 O(1)
#       하지만, 삭제된 요소 이후의 모든 요소가 메모리에서 앞으로 이동해야 하므로
#       실제로는 O(N)의 시간이 소요될 수 있습니다.

# *3)
# index() : 입력된 값을 리스트에서 찾아 그 위치를 반환하는 함수입니다.


