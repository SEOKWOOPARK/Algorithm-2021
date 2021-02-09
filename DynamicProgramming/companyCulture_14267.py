import sys
sys.setrecursionlimit(1000000)

def nextStep(transmission, nextTaker): # transmission: 전달되는 칭찬, nextTaker: 전달받을 직원
	transmission += praise[nextTaker] 
		# 현재 직원이 전달받은 칭찬 + 현재 직원이 전달해줄 칭찬 누적 => 다음 부하직원에게 넘길 준비
	praise[nextTaker] += (transmission - praise[nextTaker])
		# 현재 직원이 직속 상사로부터 받은 칭찬을 누적
	for i in sub[nextTaker]: # DFS로 자신이 받은 칭찬 부하들에게 하달.
		nextStep(transmission, i)

input = sys.stdin.readline
n, m = map(int, input().split())
boss = list(map(int, input().split()))
sub = [[] for i in range(n)]
praise = [0 for i in range(n)]

for i in range(n):
	boss[i] -= 1 # 부하직원 배열인 sub를 편하게 만들기 위한 작업

for j in range(m):
	i, w = map(int, input().split())
	praise[i - 1] += w

for i in range(n):
	if boss[i] != -2:
		sub[boss[i]].append(i)

nextStep(0,0)

for i in praise:
    print(i)