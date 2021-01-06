import sys

l = int(sys.stdin.readline())
s = input()

def makeTable(pattern):
	table = [0] * l
	j = 0
	for i in range(1, l):
		while j > 0 and pattern[i] != pattern[j]:
			j = table[j - 1]

		if pattern[i] == pattern[j]:
			j += 1
			table[i] = j
	return l - table[l - 1]

print(makeTable(s))

# KMP 알고리즘 참고