import math

def combi(n, r):
    f = math.factorial
    return f(n) / (f(r) * f(n - r))

T = int(input())
results = []

for i in range(T):
    N, M = map(int, input().split())
    results.append(int(combi(M, N)))

for result in results:
    print(result)

# 겹치면 안된다는 뜻이 교차하면 안된다는 뜻인줄 알고 시간 소요.
# 뜻만 이해하면 난이도가 높지 않다.