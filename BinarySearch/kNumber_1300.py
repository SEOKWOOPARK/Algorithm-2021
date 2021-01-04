import sys

input = sys.stdin.readline
n = int(input())
target = int(input())

low = 0
high = target
answer = 0

while low <= high:
	m = (low + high) // 2
	count = 0
	for i in range(1, n + 1):
		count = count + min(m // i, n)

	if count < target:
		low = m + 1
	else:
		answer = m
		high = m - 1

print(answer)


