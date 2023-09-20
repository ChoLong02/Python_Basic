# 컬렉션 타입
#  - 변수 하나에 값을 여러개 저장
#  - 실질적으로 변수에 컬렉션 1개가 저장
#  - 리스트(List), 튜플(Tuple), 딕트(Dictionary), 세트(Set)

# 1. 리스트(List)   ex) 기차!
#  - 시퀀스 자료형(연속 된 값 저장)
#  - 대가로 사용 []
#  - 정렬 가능
#  - mutable(생성 된 후 변경 가능)
#  - index 사용(Slicing 가능)
#  - paking과 unpaking 가능
#  - 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), 등등
# * 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]

print(list_c[0])    # 리스트에서 단일 값 추출
print(list_c[1:3])  # 리스트 슬라이싱

# 패킹과 언패킹
list_d = ["A", "B", "C"]  # 패킹
a, b, c = list_d  # 언패킹
# a = list_d[0]
# b = list_d[1]
# c = list_d[2]

# append(): 리스트 맨 마지막에 값 추가!
a = [1, 2, 3, 4, 5]
a.append(10)
print(a)

# insert(): 원하는 인덱스에 값 추가!
a.insert(1, "A")  # (인덱스, 값)
print(a)

# extend(): 리스트 병합(List A + List B)
a = [1, 2, 3]
b = [3, 4, 5]
# a.append(b) -> [1, 2, 3, [3, 4, 5]]
# a.extend(b)  # a를 기준으로 병합
# print(a)
print(a + b)

# remove(): 값으로 삭제
a = ["a", "b", "c"]
a.remove("b")
print(a)

# pop(): # 인덱스로 삭제
b = ["a", "b", "c"]
c = b.pop(0)  # 값을 삭제 전 변수에 담아서 삭제 후에 사용 가능!(선택사항)
print(b)
print(c)

# index(): 찾고자 하는 값의 인덱스 반환
a = [1, 2, 3]
print(a.index(3))  # 인덱스 반환

# sort() and sorted(): 리스트 값 정렬!
#  - sort(): 원본 값 정렬(주의: 보통 원본 값을 수정 하는 경우 극히 드뭄)
#  - sorted(): 복제 한 값 정렬
a = [9, 3, 2, 1, 5, 8, 10]
b = sorted(a)  # 오름차순
c = sorted(a, reverse=True)  # 내림차순
print(a)
print(b)
print(c)


