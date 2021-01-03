import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input()))

def solution():
	answer = 0

	for i in range(n):
		for j in range(0, i + 1):
			answer += arr[j]
	
	return answer

print(solution())


