import sys
input = sys.stdin.readline
i = 1

while True:
    l, p, v = map(int, input().split())
    if l + p + v == 50:
        print('hi')
