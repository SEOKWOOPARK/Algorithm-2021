import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
fibo = [1, 1] + [0] * (N + 1) # 피보나치 편의를 위해 [1, 1] 껴주고 시작
vip = [0]
gap = []
answer = 1

for i in range(2, len(fibo)): # 피보나치 수열 만드는 부분
    fibo[i] = fibo[i - 1] + fibo[i - 2]

for i in range(M):
    vip.append(int(input()))

vip.append(N + 1)
# vip석을 통해서 일반석의 길이를 구하기 위해 양 끝의 값은 1과 (N + 1)로 박아둔다.

for i in range(1, len(vip)):
    gap.append(vip[i] - vip[i - 1] - 1)
    # 연속된 일반석들의 길이를 구해준다.

for i in range(len(gap)):
    answer *= fibo[gap[i]]

print(answer)
