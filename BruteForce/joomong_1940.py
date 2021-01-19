# ------------------------------------
# 시간 초과
from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
base = list(combinations(list(map(int, input().split())), 2))
c = 0

for i in range(len(base)):
	if sum(base[i]) == M:
		c += 1

print(c)
# 브루트포스는 메모리 여유가 별로 없다. 따라서 정렬이나 break를 통해 짧고 효율적인 방법을 생각해야 할 때도 있다. 
# 이 문제는 정렬 후 양 끝값을 뽑아서
# 타겟인 M과 맞는지 비교하고 크면 오른쪽 인덱스를 화나 줄여서 비교한다.
# 작다면 왼쪽 인덱스를 늘려서 다시 비교한다.
# 처음 시도했던 permutations, combinations가 능사가 아니다.

# ------------------------------------

import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
K = list(map(int, input().split()))
K.sort() 
c = 0 # 가능한 갑옷을 카운팅
start = 0
end = N - 1

while start < end: # 처음 시작 인덱스가 맨끝 인덱스보다 작은 범위
	current = K[start] + K[end] # 각 조합을 합한 값, 기준 M과 비교할 값
	if current == M: # M이랑 같을 땐 start, end 인덱스를 각각 더하고 뺀다.
		c += 1
		end -= 1
		start += 1
	elif current < M: # 작을 땐 end 인덱스는 이미 최대이므로 start를 당겨온다.
		start += 1
	else: # 클 때 start 인덱스는 이미 최소. end 인덱스를 당겨온다.
		end -= 1

print(c)
