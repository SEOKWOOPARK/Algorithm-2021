import sys

input = sys.stdin.readline
n = int(input())
N = sorted(list(map(int, input().split()))) #기준 참고 배열 정렬
m = int(input())
M = list(map(int, input().split()))

def binarySearch(target, N, start, end):
	if start > end:
		return 0
	m = (start + end) // 2

	if target == N[m]:
		return 1
	elif target < N[m]:
		return binarySearch(target, N, start, m - 1)
	else:
		return binarySearch(target, N, m + 1, end)

for target in M:
	start = 0
	end = len(N) - 1
	print(binarySearch(target, N, start, end))

# 숫자카드(10815) 문제와 매우 유사하다
# 기본적인 이분탐색 문제

