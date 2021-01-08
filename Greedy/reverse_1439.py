s = input()
x = 0
y = 0

if s[0] == '0':
	x += 1
else:
	y += 1

for i in range(1, len(s)):
	if s[i] != s[i - 1]:
		if s[i] == '0':
			x += 1
		else:
			y += 1

if x >= y:
	print(y)
else:
	print(x)
# 0과 1로 바뀌는 각각의 횟수를 구하고 적은 쪽을 고른다

#-----------------------------------------------

S = input()
c = 0

for i in range(len(S) - 1):
	if S[i] != S[i + 1]:
		c += 1

print((c + 1) // 2)
# 0, 1이 두번 바뀔 때 count가 한 번이지만 마지막 숫자는 안바뀌어도 count에 1 더하고 '//' 연산을 친다.