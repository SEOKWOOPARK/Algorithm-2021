s = input().strip()
alphabet = list(range(97, 123))

for i in range(len(alphabet)):
	alphabet[i] = chr(alphabet[i])
	# chr()을 통해 아스키코드 변환. chr(97) = 'a'
	# 반대로 아스키 코드에서 숫자. ord("a") = 97
	# 대문자 범위는 65 ~ 90

for i in range(len(alphabet)):
	if s.find(alphabet[i]) > -1:
		alphabet[i] = s.find(alphabet[i])
	elif s.find(alphabet[i]) == -1:
		alphabet[i] = -1

print(*alphabet)

