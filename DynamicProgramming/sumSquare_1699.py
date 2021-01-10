import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
square = [(i * i) for i in range(1, 317)]

for i in range(1, n + 1):
	s = []
	for j in square:
		if j > i:
			break
		s.append(dp[i - j])

print(dp[n])
