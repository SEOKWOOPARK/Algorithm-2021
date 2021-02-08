import sys
input = sys.stdin.readline

N = int(input())
D = [[1, 1, 1] for i in range(N)]

for i in range(1, N):
	D[i][0] = (D[i - 1][1] + D[i - 1][2]) % 9901
	D[i][1] = (D[i - 1][0] + D[i - 1][2]) % 9901
	D[i][2] = (D[i - 1][0] + D[i - 1][1] + D[i - 1][2]) % 9901

print(sum(D[N]) % 9901)



