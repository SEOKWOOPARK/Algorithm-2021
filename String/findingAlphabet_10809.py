s = input().strip()
alphabet = list(range(97, 123))

for i in range(len(alphabet)):
	alphabet[i] = chr(alphabet[i])

for i in range(len(alphabet)):
	if s.find(alphabet[i]) > -1:
		alphabet[i] = s.find(alphabet[i])
	elif s.find(alphabet[i]) == -1:
		alphabet[i] = -1

print(*alphabet)

