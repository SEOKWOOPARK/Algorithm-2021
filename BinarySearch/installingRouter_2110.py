import sys

input = sys.stdin.readline
N, C = map(int, sys.stdin.readline().split())
ap = [int(input()) for _ in range(N)]
ap.sort()
answer = 0

def solve(minimum , maximum):
	if minimum > maximum:
		return

	dist = (maximum + minimum) // 2
	cnt = 1
	target = 0

	for idx in range(N):
		if ap[idx] >= ap[target] + dist:
			cnt += 1
			target = idx

	if cnt >= C:
		global answer
		answer = max(answer, dist)
		solve(dist + 1, maximum) # cnt가 같거나 큰 경우 중간값 이후부터 끝까지 탐색
	else: 
		solve(minimum, dist - 1) # cnt가 더 작으면 처음부터 중간값 이전까지 탐색

solve(1, (ap[-1] - ap[0]) // (C - 1) + 1)
# 1부터 5(주어진 시작값 1과 9의 중간값)까지 max,min으로 설정
print(answer)
