import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
last = set() 

for i in num: # 중복을 없애기 위해 set.add로 숫자를 필터링 선별
	last.add(i)

last = list(last) # 정렬기능을 위해 list로 감싸기
last.sort()

print(*last)

# set으로 중복 없애기 -> 정렬을 위해 list로 맵핑 -> 정렬 후 출력



