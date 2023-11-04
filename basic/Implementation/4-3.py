# 왕실의 나이트 - 구현
# 수평으로 두간 이동 후 수직으로 한칸
# 수직으로 두칸 이동 후 수평으로 한칸
#
# 좌표는  8x8
#
# 행 위치는 숫자 1~8
# 열 위치는 영어 a~h

loc = input()
x = int(loc[-1]) #행 (두번쨰자리)

loc_y = loc[:1] #열 (첫번쨰자리)
y_data = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = y_data.index(loc_y) #왜 find()는 에러나지?

nx = [0, 0, 2, -4]
ny = [2, -4, 0, 0]
ny2 = [1, -2]
count = 0
print("----------------------")
print(f"(x:{x}, y:{y})")
print("----------------------")
for i in range(4):
    # 수직으로 두칸 이동 후 수평으로 한칸 0 1
    # 수평으로 두칸 이동후 수직으로 한칸 2 3
    x += nx[i] #0 / 1
    y += ny[i] #0 / 1

    if i == 0 or i == 1:
        # 수평으로 한칸
        print("--------수평으로 두칸-------")
        print(f"(x:{x}, y:{y})")
        for j in range(2):
            print("--------수직으로 한칸-------")
            x += ny2[j]
            print(f"(x:{x}, y:{y})")
            if 0<x<9 and 0<y<9:
                print(f"*****************count (x:{x}, y:{y})")
                count += 1

    else:
        # 수직으로 한칸
        print("--------수직으로 두칸-------")
        print(f"(x:{x}, y:{y})")
        for j in range(2):
            print("--------수평으로 한칸-------")
            y += ny2[j]
            print(f"(x:{x}, y:{y})")
            if 0<x<9 and 0<y<9:
                print(f"*****************count (x:{x}, y:{y})")
                count += 1

print(count)



