import sys

N = int(sys.stdin.readline())
answer = []

for i in range(N):
	word = input()
	check = []
	check.append(word[0]) # 첫 글자 넣고 시작

	for j in range(1, len(word)):
		if check.count(word[j]) == 0 or (check.count(word[j]) >= 1 and check[-1] == word[j]):
			check.append(word[j])
		# 처음 출현했거나 두 번 이상 출현했는데 전 글자와 연속일 경우 문제의 조건 만족	
		else:
			break # 조건 안맞으면 반복문 탈출
	
	if len(check) == len(word): #원래 글자수랑 맞는지 확인
		answer.append(word)

print(len(answer))
# set으로 풀려다가 배열이 더 적합해서 방향 전환
