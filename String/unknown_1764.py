import sys

M, N = map(int, sys.stdin.readline().split())
a = set([])
b = set([])
# 각 문자열을 묶음을 set으로 받는다 => 듣, 보 모두 중복은 없지만 & 연산자 사용 목적

for i in range(N):
	a.add(sys.stdin.readline().strip())

for i in range(M):
	b.add(sys.stdin.readline().strip())

mutual = list(a & b)
# a & b => 배열을 감싼 set끼리 '&'연산할 때 공통된 것을 골라준다.
# 반복문을 아래에서 돌려야하니까 list로 a & b를 한 번더 맵핑
# '|' -> set끼리 합집합을 다뽑아준다 

print(len(mutual))

for m in sorted(mutual): # 정렬 -> 사전순 출력
	print(m)


# set.add(x) => set에 x원소 추가
# set.remove(x) => set에 x원소 삭제


