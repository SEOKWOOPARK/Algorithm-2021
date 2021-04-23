import sys
import collections

input = sys.stdin.readline
r, c, k = map(int, input().split())
A = [list(map(int, input.split()))for i in range(3)]
t = 1

while t:
    if len(A) >= len(A[0]): # 행이 더 길때
        rowLength = []
        for i in range(len(A)): # 각 행기준으로 탐색
            check = collections.Counter(A[i]) # 행마다 빈도체크
            check = check.items() # (넘버, 빈도)
            check.sort(key = lambda x : (x[1], x[0])) # 빈도, 숫자 크기순 정렬
            new = []
            for x in range(len(check)): # 정렬 결과 기존 배열에 갱신
                for y in range(len(check[x])):
                    new.append(check[x][y])            
            A[i] = new
            rowLength.append(len(new))
            
        # 길이 가장 긴 행 구하기
        m = max(rowLength)
        
        for i in range(len(A)):
            for j in range(m - len(A)[i]):
                A[i].append(0)
        
        if A[r - 1][c - 1] == k:
            return
        
        if t > 100:
            break
            
        t += 1
        
    else: # 열이 더 길때
        colLength = []
        for i in range(len(A)):
            col = [c[i] for c in A]
            check = collections.Counter(col)
            check = check.items()
            check.sort(key = lambda x : (x[1], x[0]))
            new = []
            for x in range(len(check)):
                for y in range(len(check[x])):
                    new.append(check[x][y])
            A[i] = new
            colLength.append(len(new))
            
        m = max(colLength)    
    