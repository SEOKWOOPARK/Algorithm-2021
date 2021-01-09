import sys

N = int(sys.stdin.readline())
dp = [1] * 10

for i in range(N):
	case = int(sys.stdin.readline())
	li = [[0] * 10 for i in range(case)]

	for j in range(len(li)):
		if j == 0: # 첫째자리 케이스만 처음 선언된 dp 사용
			for x in range(len(li[j])):
				li[j][x] = int((dp[x] * (dp[x] + 1)) / 2)
		elif j > 0: # 이전 값들을 활용
			for x in range(len(li[j])):
				li[j][x] = int(sum(li[j - 1][:x + 1]))

	print(sum(li[-1]))


# 1자리인 경우
# arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] => 총 10개 가능
# 2자리인 경우
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => 총 55개 가능
# 3자리인 경우
# arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55] => 총 220개 가능