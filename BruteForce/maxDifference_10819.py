import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
answer = 0

li.sort() # 정렬 한 번

if n % 2 == 0: # 주어진 숫자가 짝수개일 때
	half = (n // 2)
	a = sorted(li[:half])
	b = sorted(li[half:])

	for i in range(len(a)):
		if i != len(a) - 1:
			answer += abs(a[i] - b[i]) + abs(a[i] - b[i + 1])
		else:
			answer += abs(a[i] - b[i])

else: # 주어진 숫자가 홀수개일 때
	half = (n // 2)
	a = sorted(li[:half])
	b = sorted(li[half + 1:])
	# 딱 가운데 인덱스는 일단 뺴고 좌우로 나누어서 분리

	for i in range(len(a)):
		if i != len(a) - 1:
			answer += abs(a[i] - b[i]) + abs(a[i] - b[i + 1])
		else:
			answer += abs(a[i] - b[i])

	# li = [1, 4, 8, 9, 10, 15, 20] => a = [1, 4, 8] b = [10, 15, 20] li[half] = 9
	# last => 아직 처리안한 가운데 값, 좌측과 우측의 끝값 차이와 비교해서 큰 쪽으로 결정
	last = abs(a[-1] - c) if (abs(a[-1] - c) > abs(b[0] - c)) else abs(b[0] - c)
	answer += last

print(answer)


# ------------- 순열을 이용한 풀이

import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
permutation = list(permutations(a, n)) # 주어진 배열의 가능한 모든 배치
answer = 0

for i in permutaion:
	accumulation = 0
	li = list(i) # 두 개씩 뽑힌 튜플을 리스트로 바꾼다
	for j in range(1, n): # 차이값들 계산
		accumulation += abs(li[j] - li[j - 1])
	answer = max(answer, accumulation)

print(answer)
