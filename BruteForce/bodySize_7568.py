import sys

n = int(sys.stdin.readline())
student = []

for i in range(n):
	weight, height = map(int, sys.stdin.readline().split())
	student.append([weight, height])

for i in student:
	rank = 1 # 자신보다 몸무게, 키가 모두 더 큰 값일 때 올리는 카운팅.
	for j in student:
		if i[0] < j[0] and i[1] < j[1]:
			rank += 1 # 크고 무거우면 하나 늘린다. 순위가 낮아지는 것
	print(rank, end = " ")