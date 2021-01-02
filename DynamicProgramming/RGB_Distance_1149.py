import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
	homeColor = list(map(int, sys.stdin.readline().split()))
	li.append(homeColor)

for i in range(1, len(li)):
	li[i][0] = max(li[i - 1][1], li[i - 1][2]) + li[i][0]
	li[i][1] = max(li[i - 1][0], li[i - 1][2]) + li[i][1]
	li[i][2] = max(li[i - 1][1], li[i - 1][0]) + li[i][2]

print(min(li[n - 1]))

# 각 행에서 나올 수 있는 최솟값을 DP를 통해 할당해준다. RGB색이기 때문에 3가지만 직접 하면 해결.