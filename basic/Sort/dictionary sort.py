#딕셔너리 (key:value 형태)
d = dict()
d['a']=66
d['i']=20
d['e']=30
d['d']=33
d['f']=50
d['g']=60
d['c']=22
d['h']=80
d['b']=1

#1.딕셔너리 출력
print("\n1.기본딕셔너리")
print(d)
# {'a': 66, 'i': 20, 'e': 30, 'd': 33, 'f': 50, 'g': 60, 'c': 22, 'h': 80, 'b': 1}

# 딕셔너리 키 정렬 오름차순(디폴트)
print("\n2. 키 정렬 sorted(d.items())")
f = sorted(d.items()) # items()는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.
print(f)
# [('a', 66), ('b', 1), ('c', 22), ('d', 33), ('e', 30), ('f', 50), ('g', 60), ('h', 80), ('i', 20)]

# 딕셔너리 키 정렬 내림차순
print("\n3. 키 정렬 sorted(d.items(), reverse=True)")
g = sorted(d.items(), reverse=True)
print(g)
# [('i', 20), ('h', 80), ('g', 60), ('f', 50), ('e', 30), ('d', 33), ('c', 22), ('b', 1), ('a', 66)]

# 딕셔너리 키만 정렬 및 출력1
print("\n4. 키만 정렬 sorted(d.keys())")
h = d.keys()
# dict_keys(['a', 'i', 'e', 'd', 'f', 'g', 'c', 'h', 'b'])
h = (list(d.keys()))
# ['a', 'i', 'e', 'd', 'f', 'g', 'c', 'h', 'b']
h = sorted(d.keys())
print(h)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# 딕셔너리 키만 정렬 및 출력2
print("\n5. 키만 정렬 sorted(d)")
i = sorted(d)
print(i)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']