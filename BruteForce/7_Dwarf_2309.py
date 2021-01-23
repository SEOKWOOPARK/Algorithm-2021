import sys
from itertools import combinations

people = []
c = 0 # 조합 배열을 조회할 인덱스 기능

for i in range(9): # people 배열에 난쟁이 키를 다 넣는다
	person = int(sys.stdin.readline())
	people.append(person)

answer = list(combinations(people, 7)) # 7명 뽑는 가능한 조합 모두 구하기

while c < len(answer):
	if sum(answer[c]) == 100:
		answer[c] = list(answer[c])
		answer[c].sort()
		print(*answer[c])
		break # 조건 만족하는 케이스구하면 끝낸다
	
	c += 1
