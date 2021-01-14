import sys

input = sys.stdin.readline
N, M = map(int, input().split())
height = [[0] * (N + 1) for i in range(N + 1)] 
# 인덱스 편의를 위해 (N + 1) * (N + 1) 
counting = 0 

for i in range(M):
	x, y = map(int, input().split())
	height[x][y] = 1
	# x => 더 큰 사람, y => 더 작은 사람, height[3][4] = 1일 때 3번이 4번보다 큰 것

for mid in range(1, N + 1):
	for row in range(1, N + 1):
		for column in range(1, N + 1):
			if (height[row][mid] == 1 and height[mid][column] == 1):
				height[row][column] = 1
				# height[a][b] == 1 , height[b][c] == 1이면 a > b > c 이므로 a > c

for i in range(1, N + 1):
	clear = 0
	for j in range(1, N + 1):
		clear += height[i][j] + height[j][i]
		# i보다 작은사람과 큰 사람의 수가 N - 1일 때 등수가 확실한 사람
	if clear == (N - 1):
		counting += 1

print(counting)

