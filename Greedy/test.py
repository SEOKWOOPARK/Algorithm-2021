import sys
input = sys.stdin.readline
i = 1

while True:
	l, p, v = map(int, input().split())
	if l + p + v == 0:
		break
	answer = (v // p) * l + min(v % p, 1)

	print('Case %d %d' %(i, answer))
	i += 1

	