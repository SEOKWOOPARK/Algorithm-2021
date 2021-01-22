import sys

N = int(sys.stdin.readline())
file = []
answer = ''

for i in range(N):
	a = input()
	file.append(a)

length = len(file[0]) # 주어진 문자열들의 길이가 똑같기 때문에 아무거나 잡는다

for i in range(length): # i -> 글자별 인덱스, j -> 단어별 인덱스
	count = 1 # 첫 번째 file[0]의 첫 글자 하나 카운트하고 시작
	for j in range(1, N): 
		# 단어는 1번째부터 N번째까지,  인덱스는 1부터 마지막 인덱스까지 전부 비교
		if file[0][i] == file[j][i]: # 글자 단위로 동일여부 체크
			count += 1

		if count == N: # 주어진 N과 동일할 때 answer에 누적한다.
			answer += file[0][i]
		else: # 하나라도 다르면 '?'로 대체
			answer += '?'

print(answer)
