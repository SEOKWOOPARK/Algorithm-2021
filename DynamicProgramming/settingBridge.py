import math

def combi(n, r):
	f = math.factorial
	return f(n) / (f(r) * f(n - r))

T = int(input())
results = []

for i in range(T):
	N, M = map(int, input().split())
	results.append(int(combi(M, N)))

for result in results:
	print(result)