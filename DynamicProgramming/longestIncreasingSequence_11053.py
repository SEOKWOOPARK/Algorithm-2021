import sys

input = sys.stdin.readline
n = int(input())
A = [int(x) for x in input().split()]
DP = [1 for i in range(n)]

for i in range(n):
	for j in range(i + 1): # 0부터 자기 자신(i)까지 범위 탐색 
		if A[i] > A[j]: # 대소 비교
			DP[i] = max(DP[i], DP[j] + 1)
			# DP[i] => 기존 자기자신까지의 증가수열 최대 길이
			# DP[j] + 1 => i보다 작은 인덱스 j의 최대 길이값 + 1(i까지 증가수열의 길이로 포함)
			# 결국 i의 DP값과 (j의 DP값 + 1)을 비교해서 값 갱신

print(max(DP))