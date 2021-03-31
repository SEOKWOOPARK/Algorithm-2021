import sys
input = sys.stdin.readline

N = int(input())
testNumber = list(map(int, input().split()))
a, b = map(int, input().split())

answer = N
for num in testNumber:
    num -= a
    if num < 0:
        continue
    answer += num // b if num % b == 0 else num // b + 1

print(answer)