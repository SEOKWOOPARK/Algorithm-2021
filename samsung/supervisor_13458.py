import sys
import math

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in range(len(A)):
    A[i] -= B # 각 시험장에서 B(총감독)이 커버할 수 있는 인원 덜기
    answer += 1 # 각 시험장 총 인원 < 총감독 감시인원이어도 총감독이 1명은 반드시 들어가야 한다
    if (A[i] / C) > 0: 
        answer += math.ceil(A[i] / C)
    	# 총감독을 빼고 각 시험장에 인원이 남았다면 인원을 C(부감독)로 나누어 올림연산
print(answer)