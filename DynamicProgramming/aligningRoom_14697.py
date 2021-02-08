import sys

a, b, c, n = map(int, sys.stdin.readline().split())
dp = [0] * 301
dp[a] = dp[b] = dp[c] = 1

for i in range(a, n + 1):
	for j in [a, b, c]:
		if i >= j and dp[i - j]:
			dp[i] = 1

print(dp[n])

# 기준점은 dp[5], dp[9], dp[12]가 된다. 가령 학생수가 10명일 때 
# 크기 5짜리 방 2개를 주면 된다. 14명일 때는 5짜리 1개, 9짜리 1개로 배정할 수 있다.
# 따라서 5부터 n까지의 값들을 계산할 때 해당 숫자의 5, 9, 12 전의 값이 1이면 
# 그 숫자는 배정이 가능한 상태이며 이 방식으로 dp 배열을 n까지 확장해나간다. 45명이어도 5 x 9(개), 9 x 5(개) 
# 둘 중 하나에만 해당되면 배정가능하므로 답은 1이 된다.
