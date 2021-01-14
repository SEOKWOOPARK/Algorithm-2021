import sys
from collections import deque

n = int(sys.stdin.readline())
original = []
copy = [[0] * n for i in range(n)]
countA = 0
countB = 0

def BFS(x, y, List):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  color = List[x][y] # color => 상하좌우 비교할 때 동일여부 체크하기위한 장치
  List[x][y] = 0

  queue = deque([])
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (0 <= nx < n) and (0 <= ny < n):
        if List[nx]n[y] == color:
          List[nx][ny] = 0
          queue.append((nx, ny))

for i in range(n): # 정상인용
  original.append(list(map(str, input())))

for i in range(n): # copy 배열을 색맹용으로 설정
  for j in range(n):
    if original[i][j] == "R" or original[i][j] == 'G':
      copy[i][j] = 1 # R, G 같은 종류로 묶기
    else: # B는 다른 종류로 할당
      copy[i][j] = 2

for i in range(n): # 정상인용, 색맹용을 한꺼번에 BFS 돌린다.
  for j in range(n):
    if original[i][j] != 0:
      BFS(i, j, original)
      countA += 1 # 정상인용 영역의 R, G, B 종류 number
    if copy[i][j] != 0:
      BFS(i, j, copy)
      countB += 1 # 색맹용 영역의 (R, G), B 종류 number

print(countA, countB)

