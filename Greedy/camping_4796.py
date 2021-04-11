import sys
input = sys.stdin.readline
i = 1

while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0: # 모두 0, 0, 0일 경우 루프 탈출
        break
    answer = (v // p) * l + min(v % p, l)
    # 첫 번쨰 샘플에서 20일동안 (5 of 8 == v // p)이 두 번있고 5일이 한 번 남는다
    print('Case %d %d' %(i, answer))
    i += 1

