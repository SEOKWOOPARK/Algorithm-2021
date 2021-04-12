import sys

input = sys.stdin.readline
a = int(input())
A = list(map(int, input().split()))
A.sort() # 이분탐색은 정렬된 상태에서 해야 한다.
b = int(input())
B = list(map(int, input().split()))

def binarySearch(target, A, start, end):
    if start > end: # 범위초과, 탐색실패
        return 0
    medium = (start + end) // 2

    if target == A[medium]:
        return 1
    elif target < A[medium]:
        return binarySearch(target, A, start, medium - 1)
		# medium번째 값보다 작아서 범위를 반으로 줄일 때 처음부터 medium - 1까지만 탐색한다.
    else:
        return binarySearch(target, A, medium + 1, end)
        # medium번째 값보다 크다. 범위를 반으로 줄일 때 medium + 1부터 끝까지 탐색한다.

for target in B:
    start = 0
    end = len(A) - 1
    print(binarySearch(target, A, start, end))

