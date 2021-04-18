import sys

n, k = map(int, sys.stdin.readline())
dp = [0 for i in range(k + 1)]
dp[0] = 1 # 가능한 경우가 하나일 떄 디폴트로 메모이제이션할 기준값 셋팅
c = [] # 동전 종류가 들어갈 배열

for i in range(n):
	c.append(int(sys.stdin.readline()))


for i in c:
	for j in range(1, k + 1):
		if j - i >= 0:
			dp[j] += dp[j - i]

print(dp[k])